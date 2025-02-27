def prime_factors(l):
    return set((factor for el in l for factor in filter(lambda f: all((f % d != 0 for d in range(2, int(f ** 0.5) + 1))), range(2, el + 1))))