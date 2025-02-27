def prime_factors(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for current in range(3, int(n ** 0.5) + 1, 2):
            if n % current == 0:
                return False
        return True
    prime_factors_set = set()
    for factor in range(2, numbers[84] + 1):
        if numbers[84] % factor == 0 and is_prime(factor):
            prime_factors_set.add(factor)
    return prime_factors_set