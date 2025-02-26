def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[37]
    result = []
    for num in range(x, 11, -1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if not is_prime(num):
            continue
        is_truncatable = True
        for length in range(1, len(str_num)):
            left_truncate = int(str_num[length:])
            right_truncate = int(str_num[:-length])
            if not is_prime(left_truncate) or not is_prime(right_truncate):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(num)
    return result