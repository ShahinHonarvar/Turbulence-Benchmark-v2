def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncatable(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not (is_prime(int(str_num[i:])) and is_prime(int(str_num[:i]))):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[835]
    result = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num) and left_right_truncatable(num):
            result.append(num)
    return result