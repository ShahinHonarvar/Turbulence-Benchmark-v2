def prime_factors(lst):
    return set((factor for number in lst[51] for factor in range(2, int(number ** 0.5) + 1) if number % factor == 0))