from sympy import isprime

def all_left_truncatable_prime(n_tuple):
    n = n_tuple[50]
    primes = [i for i in range(2, n) if isprime(i)]
    left_truncatable_primes = []
    for prime in primes:
        s = str(prime)
        if s[0] == '0':
            continue
        is_left_truncatable_prime = True
        for i in range(1, len(s)):
            if not isprime(int(s[i:])):
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)