def prime_factors(l):
    i = 849
    num = l[i]
    factors = set()
    d = 2
    while d * d <= num:
        while num % d == 0:
            factors.add(d)
            num //= d
        d += 1
    if num > 1:
        factors.add(num)
    return factors