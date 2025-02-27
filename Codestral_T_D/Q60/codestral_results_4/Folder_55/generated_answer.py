def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncated_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def right_truncated_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True

def all_left_right_truncatable_prime(t):
    x = t[73]
    return sorted([i for i in range(2, x + 1) if left_truncated_prime(i) and right_truncated_prime(i)], reverse=True)