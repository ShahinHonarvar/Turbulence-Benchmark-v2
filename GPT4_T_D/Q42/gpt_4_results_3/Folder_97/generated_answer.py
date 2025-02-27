import sympy

def prime_factors(lst):
    num = lst[132]
    return set(sympy.factorint(num).keys())