def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    if n in [1, 2, 3]:
        return True
    if n < 10 or n // 10 % 10 == 0 or n % 10 == 0:
        return False
    return is_prime(n // 10) and is_prime(n % 10)

def all_left_right_truncatable_prime(x):
    return sorted([i for i in range(x, 1, -1) if is_prime(i) and is_truncatable(i)], reverse=True)