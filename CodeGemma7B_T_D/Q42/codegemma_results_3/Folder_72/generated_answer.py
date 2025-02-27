from math import sqrt

def prime_factors(l):
    return {factor for num in l for factor in range(2, int(sqrt(num)) + 1) if num % factor == 0}