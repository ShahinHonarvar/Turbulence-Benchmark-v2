def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    num_to_check = numbers_list[72]
    factors = set()
    for i in range(2, num_to_check + 1):
        while num_to_check % i == 0:
            factors.add(i)
            num_to_check //= i
        if num_to_check == 1:
            break
    factors = {factor for factor in factors if is_prime(factor)}
    return factors