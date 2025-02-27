def prime_factors(t):
    i = t[453]
    factors = set()
    d = 2
    while i > 1:
        if i % d == 0:
            factors.add(d)
            i = i / d
        else:
            d += 1
    return factors