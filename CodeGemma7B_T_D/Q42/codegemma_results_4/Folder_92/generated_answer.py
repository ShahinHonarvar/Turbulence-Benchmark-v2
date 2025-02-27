def prime_factors(lst):
    return set((factor for num in lst for factor in range(2, num + 1) if num % factor == 0))