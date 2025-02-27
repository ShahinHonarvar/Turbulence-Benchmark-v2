import sympy 

def composite_nums_between_indices(lst):
    return set((x for x in lst[49:55] if sympy.isprime(x) == False))