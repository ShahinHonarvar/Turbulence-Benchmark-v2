def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_leftmost_digit(n):
    return int(str(n)[1:])

def remove_rightmost_digit(n):
    return int(str(n)[:-1])

def is_left_right_truncatable_prime(n):
    if not is_prime(n) or '0' in str(n):
        return False
    while n > 9:
        n = remove_leftmost_digit(n)
        if not is_prime(n):
            return False
        n = remove_rightmost_digit(n)
        if not is_prime(n):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[803]
    result = []
    for i in range(1, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return result