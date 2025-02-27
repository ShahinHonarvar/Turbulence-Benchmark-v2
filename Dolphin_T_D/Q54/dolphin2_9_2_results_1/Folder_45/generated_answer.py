import sympy

def all_right_truncatable_prime(x):
    return sorted([i for i in sympy.primerange(2, x) if str(i)[-1:] in '137' and all((sympy.isprime(int(str(i)[:-j])) for j in range(1, len(str(i)))))])