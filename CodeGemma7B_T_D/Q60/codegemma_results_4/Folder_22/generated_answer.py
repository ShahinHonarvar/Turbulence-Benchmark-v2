import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[85]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_primes = []
    for p in primes:
        str_p = str(p)
        if '0' not in str_p:
            for i in range(1, len(str_p)):
                left = int(str_p[i:])
                right = int(str_p[:-i])
                if is_prime(left) and is_prime(right):
                    truncatable_primes.append(p)
    truncatable_primes.sort()
    return truncatable_primes