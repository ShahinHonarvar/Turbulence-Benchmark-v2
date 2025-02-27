import itertools

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

def right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 9:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[13]
    return sorted([i for i in range(1, x) if right_truncatable_prime(i)])