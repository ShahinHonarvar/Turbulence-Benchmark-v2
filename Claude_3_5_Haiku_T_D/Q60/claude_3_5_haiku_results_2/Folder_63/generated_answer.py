def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[88]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_truncatable(num):
            result.append(num)
    return sorted(result)

def is_truncatable(n):
    str_num = str(n)
    for i in range(1, len(str_num)):
        left_trunc = int(str_num[i:])
        right_trunc = int(str_num[:-i])
        if not (is_prime(left_trunc) and is_prime(right_trunc)):
            return False
    return is_prime(n)