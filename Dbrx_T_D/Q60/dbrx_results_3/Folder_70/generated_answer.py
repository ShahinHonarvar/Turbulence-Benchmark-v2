from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[433]
    primes = [i for i in range(1, x + 1) if isprime(i) and (not '0' in str(i))]
    result = []
    for p in primes:
        if is_left_right_truncatable_prime(p, 10):
            result.append(p)
    return sorted(result, reverse=True)

def is_left_right_truncatable_prime(n, base):
    if n < base:
        return True
    if not isprime(n):
        return False
    if n % base == 0:
        return False
    return is_left_right_truncatable_prime(int(str(n)[1:]), base) and is_left_right_truncatable_prime(int(str(n)[:-1]), base)