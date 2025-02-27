import sympy

def prime_factors(numbers):
    return set(sympy.primerange(2, numbers[126] + 1))