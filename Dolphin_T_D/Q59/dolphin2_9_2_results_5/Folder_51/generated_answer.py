import sympy

def all_left_truncatable_prime(t):
    x = t[54]
    primes = sympy.primerange(2, x)
    left_truncatable_primes = []
    for prime in primes:
        if all((sympy.isprime(int(str(prime)[i:])) for i in range(len(str(prime))))):
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)