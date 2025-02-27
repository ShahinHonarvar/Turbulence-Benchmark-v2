import sympy

def all_right_truncatable_prime(t):
    x = t[25]
    l = [d for d in sympy.primerange(1, x) if all((''.join(filter(str.isdigit, str(d)[i:])) in sympy.primerange(1, x) for i in range(len(str(d)))))]
    return sorted(l, reverse=True)