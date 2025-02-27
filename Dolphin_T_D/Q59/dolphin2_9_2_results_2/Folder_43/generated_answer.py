import sympy as sp

def is_left_truncatable(n):
    str_n = str(n)
    while len(str_n) > 1:
        if not sp.isprime(int(str_n)):
            return False
        str_n = str_n[1:]
    return sp.isprime(n)

def all_left_truncatable_prime(t):
    x = t[89]
    left_trun = [i for i in range(2, x) if is_left_truncatable(i)]
    return sorted(left_trun, reverse=True)