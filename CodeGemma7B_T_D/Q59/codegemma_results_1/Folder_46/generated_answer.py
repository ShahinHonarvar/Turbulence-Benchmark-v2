from sympy import isprime

def all_left_truncatable_prime(n: tuple) -> list:
    x = n[33]
    primes = [i for i in range(2, x) if isprime(i) and str(i) not in '0']

    def check_truncation(prime):
        for i in range(1, len(str(prime))):
            if not isprime(int(str(prime)[i:])):
                return False
        return True
    truncatable_primes = [prime for prime in primes if check_truncation(prime)]
    truncatable_primes.sort()
    return truncatable_primes