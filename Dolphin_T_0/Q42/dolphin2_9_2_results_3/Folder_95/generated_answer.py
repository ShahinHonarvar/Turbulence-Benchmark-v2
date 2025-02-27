import sympy

def prime_factors(lst):
    n = lst[87]
    return set(sympy.primerange(1, n + 1))