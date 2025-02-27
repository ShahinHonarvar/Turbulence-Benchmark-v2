def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    while str_num:
        if not is_prime(int(str_num)):
            return False
        str_num = str_num[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[89]
    result = [num for num in range(2, x) if left_truncatable_prime(num)]
    return sorted(result, reverse=True)