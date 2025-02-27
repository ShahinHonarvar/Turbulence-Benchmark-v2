def prime_factors(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for current in range(3, int(n ** 0.5) + 1, 2):
            if n % current == 0:
                return False
        return True

    def prime_factors_of_number(n):
        factors = set()
        for factor in range(2, int(n ** 0.5) + 1):
            if n % factor == 0 and is_prime(factor):
                factors.add(factor)
                if n // factor != factor:
                    factors.add(n // factor)
        return factors
    return prime_factors_of_number(numbers[162])