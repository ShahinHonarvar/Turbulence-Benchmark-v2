def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[88]
    result = []
    for num in range(x, 1, -1):
        if is_prime(num) and is_left_right_truncatable(num):
            result.append(num)
    result.sort(reverse=True)
    return result

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable(num):
    if '0' in str(num):
        return False
    num_str = str(num)
    for i in range(1, len(num_str)):
        left_truncated = int(num_str[i:])
        right_truncated = int(num_str[:-i])
        if not is_prime(left_truncated) or not is_prime(right_truncated):
            return False
    return True