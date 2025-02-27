def is_left_right_truncatable_prime(n):
    if n < 10:
        return False
    while n != 0 and n != 1:
        n = int(n / 10)
        if is_prime(n):
            n = int(n / 10)
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(a):
    x = a[645]
    return sorted([i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)])