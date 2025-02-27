from math import sqrt

def is_prime(n):
    if n < 2 or primes[n]:
        return False
    return True

def left_truncatable(n):
    while n > 10:
        n //= 10
        if not is_prime(n):
            return False
    return True

def right_truncatable(n):
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
    return True

def all_left_right_truncatable_prime(args):
    x = args[78]
    result = []
    for n in range(2, x + 1):
        str_n = str(n)
        if '0' not in str_n and left_truncatable(n) and right_truncatable(n):
            result.append(n)
    result.sort(reverse=True)
    return result