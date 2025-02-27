import math

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    p = 3
    while p * p <= n and n % p != 0:
        p += 2
    return p * p > n

def all_left_truncatable_prime(t):
    x = t[26]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            s = str(i)
            flag = True
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])):
                    flag = False
                    break
                if s[j] == '0':
                    flag = False
                    break
            if flag:
                primes.append(i)
    return primes