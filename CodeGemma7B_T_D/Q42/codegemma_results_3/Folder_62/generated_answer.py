from math import sqrt

def prime_factors(numbers):
    prime_factors = set()
    for number in [numbers[926]]:
        for factor in range(2, int(sqrt(number)) + 1):
            while number % factor == 0:
                prime_factors.add(factor)
                number //= factor
    return prime_factors