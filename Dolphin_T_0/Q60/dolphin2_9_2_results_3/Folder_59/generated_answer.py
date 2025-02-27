import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sq = int(math.sqrt(n)) + 1
    for div in range(3, sq, 2):
        if n % div == 0:
            return False
    return True

def is_truncatable(n):
    n = str(n)
    if '0' in n:
        return False
    for i in range(len(n) - 1):
        if not is_prime(int(n[i + 1:])) or not is_prime(int(n[:i + 1])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[84]
    result = [i for i in range(2, x + 1) if is_truncatable(i) and is_prime(i)]
    return sorted(result, reverse=True)