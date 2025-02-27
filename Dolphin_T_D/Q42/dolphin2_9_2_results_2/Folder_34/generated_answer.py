from sympy import primefactors

def prime_factors(numbers):
    if len(numbers) < 98:
        raise ValueError('List is not long enough')
    return set(primefactors(numbers[97]))