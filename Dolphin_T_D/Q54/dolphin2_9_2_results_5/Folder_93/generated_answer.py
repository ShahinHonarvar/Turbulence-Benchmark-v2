def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    n = str(n)
    for i in range(len(n) - 1, 0, -1):
        if not is_prime(int(n[i:])):
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[11]
    return sorted([n for n in range(2, x) if is_truncatable_prime(n)])