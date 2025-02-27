from sympy import isprime

def all_left_right_truncatable_prime(tup):
    limit = tup[767]
    primes = [i for i in range(10, limit + 1) if isprime(i)]
    lrt_primes = [i for i in primes if is_left_right_truncatable_prime(i)]
    return sorted(lrt_primes, reverse=True)

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    while len(str(n)) > 1:
        n = int(str(n)[1:])
        if not isprime(n):
            return False
    return True