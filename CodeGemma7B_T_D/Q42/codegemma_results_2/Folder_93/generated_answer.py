def prime_factors(x):
    return {i for i in range(2, x) if x % i == 0}