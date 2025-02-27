def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    n_str = str(n)
    if '0' in n_str or len(n_str) < 2:
        return False
    last_digit_idx = len(n_str) - 1
    while last_digit_idx > 0:
        if not is_prime(int(n_str[last_digit_idx:])):
            return False
        last_digit_idx -= 1
    first_digit_idx = 0
    while first_digit_idx < last_digit_idx:
        if not is_prime(int(n_str[:first_digit_idx + 1])):
            return False
        first_digit_idx += 1
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[86]
    return [n for n in range(2, x + 1) if is_truncatable_prime(n)]