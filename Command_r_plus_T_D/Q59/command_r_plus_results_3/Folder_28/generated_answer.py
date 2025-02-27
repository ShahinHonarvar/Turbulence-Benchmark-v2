def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[:i])) or str_num[0] == '0':
            return False
    return True

def all_left_truncatable_prime(limit):
    result = []
    for num in range(2, limit):
        if left_truncatable_prime(num):
            result.append(num)
    return result