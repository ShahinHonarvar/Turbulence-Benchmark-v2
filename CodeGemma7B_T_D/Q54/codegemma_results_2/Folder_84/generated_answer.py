import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable(n):
    if not is_prime(n):
        return False
    for i in reversed(range(1, len(str(n)))):
        if not is_prime(int(str(n)[:-i])):
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[630]
    return sorted([n for n in range(2, x) if right_truncatable(n)], reverse=True)