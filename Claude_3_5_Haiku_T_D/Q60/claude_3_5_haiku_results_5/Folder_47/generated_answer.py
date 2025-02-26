def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    while len(str(n)) > 1:
        n_str = str(n)
        left_truncated = int(n_str[1:])
        right_truncated = int(n_str[:-1])
        if not (is_prime(left_truncated) and is_prime(right_truncated)):
            return False
        n = left_truncated if len(str(left_truncated)) >= len(str(right_truncated)) else right_truncated
    return is_prime(n)

def all_left_right_truncatable_prime(numbers):
    x = numbers[49]
    return sorted([num for num in range(2, x + 1) if is_prime(num) and is_left_right_truncatable_prime(num)])