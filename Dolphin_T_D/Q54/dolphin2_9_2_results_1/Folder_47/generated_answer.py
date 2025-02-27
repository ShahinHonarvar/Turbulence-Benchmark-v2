import sympy

def all_right_truncatable_prime(x):
    primes = list(sympy.primerange(2, x))
    right_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            if not sympy.isprime(int(str_prime[i:])):
                break
            else:
                right_truncatable_primes.append(prime)
    return sorted(list(set(right_truncatable_primes)))