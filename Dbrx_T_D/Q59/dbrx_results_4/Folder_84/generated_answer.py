from sympy import isprime

def is_left_truncatable_prime(n):
    while n > 0:
        if not isprime(n):
            return False
        n = int(str(n)[1:])
    return True

def all_left_truncatable_prime(upper_bound_tuple):
    x = upper_bound_tuple[630]
    primes = [i for i in range(1, x) if is_left_truncatable_prime(i)]
    return sorted(primes, reverse=True)