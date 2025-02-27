def all_left_right_truncatable_prime(x):
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and (not has_zero(num)) and is_truncatable(num):
            result.append(num)
    result.sort()
    return result

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def has_zero(num):
    return '0' in str(num)

def is_truncatable(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        left = int(str_num[:i])
        right = int(str_num[i:])
        if not (is_prime(left) and is_prime(right)):
            return False
    return True