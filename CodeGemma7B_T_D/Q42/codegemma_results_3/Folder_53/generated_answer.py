from math import sqrt

def prime_factors(integers):
    factors = set()
    number = integers[73]
    for factor in range(2, int(sqrt(number)) + 1):
        while number % factor == 0:
            factors.add(factor)
            number //= factor
    if number > 1:
        factors.add(number)
    return factors