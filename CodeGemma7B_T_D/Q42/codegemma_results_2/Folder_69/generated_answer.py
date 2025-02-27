from math import sqrt

def prime_factors(l):
    factors = set()
    for item in l:
        for j in range(2, int(sqrt(item)) + 1):
            if item % j == 0:
                factors.add(j)
                while item % j == 0:
                    item //= j
    return factors