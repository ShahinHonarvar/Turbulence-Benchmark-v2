def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    if num < 10 and (not is_prime(num)):
        return False
    str_num = str(num)
    for i in range(len(str_num)):
        if not is_prime(int(str_num[:i])) or int(str_num[i]) == 0:
            return False
    return True

def all_left_truncatable_prime(limit):
    result = []
    for num in range(limit[41] - 1, 1, -1):
        if left_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)