import sympy

def all_right_truncatable_prime(input_tuple):
    x = input_tuple[100]
    primes = sympy.primerange(2, x)
    right_truncatable_primes = []
    for prime in primes:
        if all((sympy.isprime(int(str(prime)[i:])) for i in range(1, len(str(prime))))):
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)