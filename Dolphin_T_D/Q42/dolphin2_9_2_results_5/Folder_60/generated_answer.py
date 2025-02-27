def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_of(n):
        factors = set()
        for i in range(2, n + 1):
            if n % i == 0:
                factors.add(i)
        for factor in list(factors):
            if is_prime(factor):
                factors.add(factor)
        return factors
    return prime_factors_of(numbers[88])