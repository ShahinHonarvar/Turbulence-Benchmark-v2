import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(t):
    x = t[77]
    primes = []
    for i in range(x, 1, -1):
        s = str(i)
        if '0' in s:
            continue
        if is_prime(i) and is_prime(int(s[1:])):
            truncatable = True
            while len(s) > 2:
                n = int(s)
                if not is_prime(n // 10) or not is_prime(n % 10):
                    truncatable = False
                    break
                s = str(n // 10)
            if truncatable:
                primes.append(i)
    return primes[::-1]