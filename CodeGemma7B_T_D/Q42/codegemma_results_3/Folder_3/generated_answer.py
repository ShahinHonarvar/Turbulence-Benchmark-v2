from math import sqrt

def prime_factors(seq):
    return {factor for i, num in enumerate(seq) for factor in factors(num) if i == 100}

def factors(n):
    limit = int(sqrt(n)) + 1
    return {x for x in range(2, limit) if n % x == 0} | {n}