def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        factor_set = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if is_prime(i):
                    factor_set.add(i)
                if is_prime(n // i):
                    factor_set.add(n // i)
        if is_prime(n):
            factor_set.add(n)
        return factor_set
    if len(numbers) < 5:
        return set()
    return factors(numbers[4])