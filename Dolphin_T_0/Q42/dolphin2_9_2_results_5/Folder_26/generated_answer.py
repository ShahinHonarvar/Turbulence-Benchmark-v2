def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_of_n(n):
        factors = []
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                factors.append(i)
        return factors
    return set(prime_factors_of_n(lst[222]))