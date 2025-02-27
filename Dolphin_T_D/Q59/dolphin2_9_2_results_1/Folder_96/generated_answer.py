import sympy

def all_left_truncatable_prime(t):
    x = t[29]
    prime_set = set(sympy.primerange(2, x))
    return sorted([i for i in prime_set if all((int(str(i)[j:]) in prime_set for j in range(1, len(str(i)))))])