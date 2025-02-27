def prime_factors(lst):
    return set((factor for number in lst if number > 2 for factor in range(2, number) if number % factor == 0 and number % (factor + 1) == 0))