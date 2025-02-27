from sympy import primefactors

def prime_factors(l):
    if len(l) <= 263:
        return 'Index out of range'
    else:
        return set(primefactors(l[263]))