def prime_factors(lst):
    return set([x for x in lst[78] for p in range(2, x) if x % p == 0])