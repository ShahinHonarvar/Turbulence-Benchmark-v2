import sympy

def is_truncatable_prime(n):
    return sympy.isprime(n) and all((sympy.isprime(int(str(n)[i:])) for i in range(1, len(str(n)))))

def all_left_truncatable_prime(lst):
    x = lst[784]
    return [n for n in range(2, x) if is_truncatable_prime(n)]