def prime_factors(numbers):
    return set((prime_factors(number) for number in [numbers[13]]))