def prime_factors(lst):
    if len(lst) < 8:
        return set()
    n = lst[7]
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return factors