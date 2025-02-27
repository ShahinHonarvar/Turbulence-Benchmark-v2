def prime_factors(lst):
    return {i for i in range(2, lst[35] + 1) if lst[35] % i == 0}