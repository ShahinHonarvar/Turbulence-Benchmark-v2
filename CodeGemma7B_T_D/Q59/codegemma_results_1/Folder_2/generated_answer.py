import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if int(str_n[i:]) % 2 == 0 or '0' in str_n[i:]:
            return False
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[618]
    left_truncatable_primes = []
    for n in range(2, x):
        if is_truncatable_prime(n):
            left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes)