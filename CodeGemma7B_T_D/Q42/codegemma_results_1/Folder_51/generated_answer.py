def prime_factors(lst):
    return set((factor for number in lst for factor in range(2, int(number ** 0.5) + 1) if number % factor == 0 and number == lst[64]))