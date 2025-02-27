def prime_factors(lst):
    target = lst[16]
    factors = set()
    d = 2
    while d * d <= target:
        if target % d == 0:
            factors.add(d)
            target //= d
        else:
            d += 1
    if target > 1:
        factors.add(target)
    return factors