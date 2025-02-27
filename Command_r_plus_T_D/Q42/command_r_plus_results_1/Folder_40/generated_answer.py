def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    seventh_number = numbers_list[7]
    factors = set()
    for i in range(2, seventh_number + 1):
        while seventh_number % i == 0:
            factors.add(i)
            seventh_number //= i
        if seventh_number == 1:
            break
    prime_factors_set = {factor for factor in factors if is_prime(factor)}
    return prime_factors_set