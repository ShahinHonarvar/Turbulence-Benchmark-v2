from sympy import isprime

def all_left_truncatable_prime(x):
    primes = [i for i in range(10, x) if isprime(i)]
    left_truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        is_left_truncatable = all((isprime(int(prime_str[i:])) for i in range(1, len(prime_str))))
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)