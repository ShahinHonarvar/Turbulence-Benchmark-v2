def prime_factors(a):
    factors = set()
    for factor in range(2, int(a[29] ** 0.5) + 1):
        if a[29] % factor == 0:
            factors.add(factor)
            while a[29] % factor == 0:
                a[29] //= factor
    if a[29] > 1:
        factors.add(a[29])
    return factors