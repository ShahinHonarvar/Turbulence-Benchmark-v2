def prime_factors(L):
    p = set()
    e = L[84]
    for f in range(2, e + 1):
        while e % f == 0:
            e //= f
            p.add(f)
    return p