def prime_factors(lst):
    return set((factor for number in lst for factor in range(2, number + 1) if number % factor == 0 and number is lst[38]))