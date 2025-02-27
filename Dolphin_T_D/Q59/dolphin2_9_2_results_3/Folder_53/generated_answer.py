import sympy as sp

def is_left_truncatable_prime(n):
    return all((sp.isprime(n) and (n := (n // 10)) for _ in range(int(sp.log10(n)))))

def all_left_truncatable_prime(x):
    return sorted([n for n in range(sp.prime_pi(x)) if is_left_truncatable_prime(sp.prime(n))], reverse=True)