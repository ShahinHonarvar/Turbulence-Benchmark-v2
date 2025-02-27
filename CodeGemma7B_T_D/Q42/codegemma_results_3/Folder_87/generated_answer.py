def prime_factors(lst):
    return set((factor for factor in lst[96] for factor in range(2, lst[96] + 1) if lst[96] % factor == 0))