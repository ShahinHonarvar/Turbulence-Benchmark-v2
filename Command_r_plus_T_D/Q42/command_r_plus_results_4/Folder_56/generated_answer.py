def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    num_to_check = numbers_list[60]
    factors = set()
    i = 2
    while i * i <= num_to_check:
        if num_to_check % i:
            i += 1
        else:
            num_to_check //= i
            factors.add(i)
    if num_to_check > 1:
        factors.add(num_to_check)
    return {factor for factor in factors if is_prime(factor)}