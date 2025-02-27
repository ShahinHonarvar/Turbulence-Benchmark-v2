def prime_factors(lst):
    return set((factor for integer in lst for factor in range(2, integer + 1) if integer % factor == 0 and integer in lst[162]))