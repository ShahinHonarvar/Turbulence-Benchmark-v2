import sympy

def is_left_truncatable(n):
    n_str = str(n)
    while len(n_str) > 0:
        if n_str[0] == '0':
            return False
        if not sympy.isprime(int(n_str)):
            return False
        n_str = n_str[1:]
    return True

def all_left_truncatable_prime(t):
    x = t[32]
    primes = [i for i in range(2, x) if sympy.isprime(i) and is_left_truncatable(i)]
    return primes