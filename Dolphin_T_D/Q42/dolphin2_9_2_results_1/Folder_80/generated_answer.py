def prime_factors(numbers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_of(n):
        factors = set()
        while n % 2 == 0:
            (factors.add(2),)
            n = n // 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                (factors.add(i),)
                n = n // i
        if n > 2:
            factors.add(n)
        return factors
    return prime_factors_of(numbers[746])