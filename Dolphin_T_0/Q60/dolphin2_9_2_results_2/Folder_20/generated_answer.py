def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
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

def left_right_truncatable_prime(n):
    if n < 2:
        return False
    x = n
    while x:
        if x < 2 or not is_prime(x):
            return False
        x //= 10
    return is_prime(n)

def all_left_right_truncatable_prime(x):
    return sorted([i for i in range(x, 1, -1) if left_right_truncatable_prime(i)])