def prime_factors(lst):

    def get_prime_factors(n):
        factors = set()
        d = 2
        while n >= d * d:
            if n % d == 0:
                factors.add(d)
                n //= d
            else:
                d += 1
        if n > 1:
            factors.add(n)
        return factors
    if 0 <= 926 < len(lst):
        return get_prime_factors(lst[926])
    return set()