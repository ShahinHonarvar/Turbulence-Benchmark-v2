def prime_factors(lst):

    def is_prime(n):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    return False
            else:
                return True
        else:
            return False

    def prime_factors(n):
        factors = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if is_prime(i):
                    factors.add(i)
                if i != n // i and is_prime(n // i):
                    factors.add(n // i)
        return factors
    return prime_factors(lst[45])