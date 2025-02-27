def prime_factors(lst):
    factors = set()
    for n in lst[162]:
        for p in range(2, n + 1):
            if n % p == 0:
                factors.add(p)
    return factors