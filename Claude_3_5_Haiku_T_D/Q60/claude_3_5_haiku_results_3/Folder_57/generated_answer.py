def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[54]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_truncatable_prime(num):
    num_str = str(num)
    if not is_prime(num):
        return False
    for i in range(1, len(num_str)):
        left_truncated = int(num_str[i:])
        right_truncated = int(num_str[:-i])
        if not is_prime(left_truncated) or not is_prime(right_truncated):
            return False
    return True