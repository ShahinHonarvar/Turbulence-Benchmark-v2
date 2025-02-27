def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_digit(n):
    return [n // 10, n % 10]

def left_right_truncatable_prime(n):
    while n:
        if len(str(n)) == 1:
            return True
        left, right = remove_digit(n)
        if not is_prime(left) or not is_prime(right):
            return False
        n = left
    return is_prime(n)

def all_left_right_truncatable_prime(t):
    x = t[758]
    return [n for n in range(2, x + 1) if left_right_truncatable_prime(n) and is_prime(n)]