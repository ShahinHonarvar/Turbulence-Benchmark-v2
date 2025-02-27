def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n <= 3:
        return False
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def right_truncatable(n):
    if is_prime(n):
        return is_prime(n // 10) if n >= 10 else False
    return False

def left_truncatable(n):
    a = 0
    while n:
        if is_prime(n):
            a = 1
        n //= 10
    return a

def all_left_right_truncatable_prime(t):
    x = t[32]
    return [i for i in range(2, x + 1) if left_truncatable(i) and right_truncatable(i)]