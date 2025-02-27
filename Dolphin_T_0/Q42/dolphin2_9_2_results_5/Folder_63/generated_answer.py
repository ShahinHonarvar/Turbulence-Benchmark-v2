def prime_factors(lst):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        factors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                if is_prime(i):
                    factors.append(i)
                if i != n // i and n // i != 1:
                    if is_prime(n // i):
                        factors.append(n // i)
        return factors
    if len(lst) > 57:
        return set(factors(lst[57]))
    else:
        return None