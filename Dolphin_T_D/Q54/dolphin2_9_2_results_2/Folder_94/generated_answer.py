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

def all_right_truncatable_prime(t):
    x = t[43]
    primes = []
    for n in range(2, x):
        while is_prime(n) and len(str(n)) > 1 and (int(str(n)[-1], n) > 1):
            n = int(str(n)[-2:])
            if n > 1 and len(str(n)) > 1:
                primes.append(n)
    return sorted(list(set(primes)))