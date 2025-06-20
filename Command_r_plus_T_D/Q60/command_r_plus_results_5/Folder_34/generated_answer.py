def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncatable_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        left_trunc = int(str_num[i:])
        right_trunc = int(str_num[:i])
        if not is_prime(left_trunc) or not is_prime(right_trunc):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    start, end = numbers
    result = []
    for num in range(end, start - 1, -1):
        if left_right_truncatable_prime(num):
            result.append(num)
    return result