import sympy

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[89]
    primes = sympy.primerange(1, x)
    right_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        while len(str_prime) > 1:
            if sympy.isprime(int(str_prime[1:])):
                str_prime = str_prime[1:]
                if len(str_prime) == 1:
                    right_truncatable_primes.append(int(str_prime))
            else:
                break
    return sorted(right_truncatable_primes, reverse=True)