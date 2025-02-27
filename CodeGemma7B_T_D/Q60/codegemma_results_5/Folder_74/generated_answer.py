def all_left_right_truncatable_prime(x):
    truncatable = []
    for num in range(2, x + 1):
        if is_prime(num) and (not contains_zero(num)):
            left_truncatable, right_truncatable = (is_left_truncatable(num), is_right_truncatable(num))
            if left_truncatable and right_truncatable:
                truncatable.append(num)
    return sorted(truncatable)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def contains_zero(num):
    return '0' in str(num)

def is_left_truncatable(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    return True

def is_right_truncatable(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[:-i])):
            return False
    return True