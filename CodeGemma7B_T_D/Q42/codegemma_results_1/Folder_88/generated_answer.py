def prime_factors(lst):
    """Don't want any comments in the code"""
    factors = set((factor for number in lst for factor in range(2, number + 1) if number % factor == 0))
    return factors