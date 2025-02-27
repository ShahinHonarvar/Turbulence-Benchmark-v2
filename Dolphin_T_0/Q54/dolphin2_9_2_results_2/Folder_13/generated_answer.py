import sympy

def all_right_truncatable_prime(x):
    primes = sympy.primerange(2, x)
    right_truncatable_primes = []
    for p in primes:
        str_p = str(p)
        for i in range(len(str_p)):
            if not sympy.isprime(int(str_p[i:])):
                break
        else:
            right_truncatable_primes.append(p)
    return sorted(right_truncatable_primes)