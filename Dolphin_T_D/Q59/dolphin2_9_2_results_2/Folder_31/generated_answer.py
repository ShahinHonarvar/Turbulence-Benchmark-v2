def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def left_truncatable(n):
    while n > 0:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[50]
    result = [n for n in range(x, 1, -1) if left_truncatable(n) and is_prime(n)]
    return result