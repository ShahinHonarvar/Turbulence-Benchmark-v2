from itertools import count

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_lrt_prime(n):
    if not is_prime(n) or '0' in str(n):
        return False
    s = str(n)
    for i in range(len(s) - 1):
        if not is_prime(int(s[i:])):
            return False
    return True

def all_left_right_truncatable_prime(x):
    lrtp = []
    primes = [p for p in range(10, x + 1) if is_prime(p)]
    for p in primes:
        if all((is_prime(int(str(p)[i:])) for i in range(1, len(str(p))))):
            lrtp.append(p)
    return sorted(lrtp, reverse=True)