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
        factors_set = set()
        d = 2
        while n >= d * d:
            if n % d == 0:
                factors_set.add(d)
                while n % d == 0:
                    n //= d
            d += 1
        if n > 1:
            factors_set.add(n)
        return factors_set
    if len(lst) > 312:
        return factors(lst[312])
    return set()