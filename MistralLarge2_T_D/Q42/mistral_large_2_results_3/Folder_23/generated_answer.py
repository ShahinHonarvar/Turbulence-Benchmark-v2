def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        factors_set = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if is_prime(i):
                    factors_set.add(i)
                if is_prime(n // i):
                    factors_set.add(n // i)
        if is_prime(n):
            factors_set.add(n)
        return factors_set
    if len(lst) > 69:
        return factors(lst[69])
    else:
        return set()