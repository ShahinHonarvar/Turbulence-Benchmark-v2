import sympy

def all_left_truncatable_prime(t):
    x = t[36]
    primes = list(sympy.primerange(1, x))
    left_truncatables = []
    for p in primes:
        if not '0' in str(p):
            is_left_truncatable = True
            for digit in str(p)[1:]:
                if not sympy.isprime(int(digit)):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatables.append(p)
    return sorted(left_truncatables)