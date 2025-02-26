def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    if '0' in str(num):
        return False
    while num > 9:
        num_str = str(num)
        left_truncated = int(num_str[1:])
        right_truncated = int(num_str[:-1])
        if not is_prime(left_truncated) or not is_prime(right_truncated):
            return False
        num = left_truncated
    return is_prime(num)

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[19]
    result = []
    for num in range(10, x + 1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)