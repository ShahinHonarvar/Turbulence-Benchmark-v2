def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(n):
    n = str(n)
    for i in range(len(n) - 1):
        if not is_prime(int(n[i:])):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[73]
    return sorted([i for i in range(x, 0, -1) if is_prime(i) and left_truncatable(i)], reverse=True)