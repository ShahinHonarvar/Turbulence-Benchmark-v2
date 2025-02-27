import sympy

def all_right_truncatable_prime(t):
    x = t[41]
    primes = []
    for n in range(2, x):
        if sympy.isprime(n):
            m = n
            while m != 0:
                if not sympy.isprime(m):
                    break
                m //= 10
            else:
                primes.append(n)
    return sorted(primes, reverse=True) or []