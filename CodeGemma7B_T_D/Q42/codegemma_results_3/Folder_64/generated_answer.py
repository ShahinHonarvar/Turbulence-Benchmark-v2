def prime_factors(lst):
    return set((factor for number in lst if number % lst[1] == 0 for factor in range(2, number)))