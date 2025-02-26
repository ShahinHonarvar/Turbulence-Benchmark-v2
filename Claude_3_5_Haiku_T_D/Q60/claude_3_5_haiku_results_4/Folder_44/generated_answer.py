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
        if not is_prime(num):
            return False
        num_str = str(num)
        num_str_left = num_str[1:]
        num_str_right = num_str[:-1]
        num = int(num_str_left)
        if not is_prime(num):
            return False
        num = int(num_str_right)
        if not is_prime(num):
            return False
    return is_prime(num)

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[39]
    result = []
    for num in range(10, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)