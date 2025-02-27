def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def factors(n):
        factor_set = set()
        d = 2
        while d * d <= n:
            while n % d == 0:
                if is_prime(d):
                    factor_set.add(d)
                n //= d
            d += 1
        if n > 1 and is_prime(n):
            factor_set.add(n)
        return factor_set
    if len(lst) > 33:
        return factors(lst[33])
    return set()