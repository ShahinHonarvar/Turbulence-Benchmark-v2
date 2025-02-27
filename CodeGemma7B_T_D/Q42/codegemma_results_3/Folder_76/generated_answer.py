def prime_factors(lst):
    return set((factor for n in lst[537] for factor in range(2, int(n ** 0.5) + 1) if n % factor == 0))