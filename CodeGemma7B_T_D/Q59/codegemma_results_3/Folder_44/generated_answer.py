from sympy import isprime

def all_left_truncatable_prime(x):
    """
    Returns all left-truncatable prime numbers less than x.
    """
    primes = [i for i in range(2, x) if isprime(i)]
    left_truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        if '0' in prime_str:
            continue
        for i in range(1, len(prime_str)):
            truncatable_prime = int(prime_str[i:])
            if not isprime(truncatable_prime):
                break
        else:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)