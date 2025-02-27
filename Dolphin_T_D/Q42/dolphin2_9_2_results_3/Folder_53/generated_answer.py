from sympy import factorint

def prime_factors(lst):
    number = lst[73]
    return set(factorint(number).keys())