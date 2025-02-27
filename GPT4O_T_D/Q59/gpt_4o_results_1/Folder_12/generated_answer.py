def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    if '0' in str(num):
        return False
    str_num = str(num)
    while str_num:
        if not is_prime(int(str_num)):
            return False
        str_num = str_num[1:]
    return True

def all_left_truncatable_prime(t):
    if len(t) <= 70:
        return []
    limit = t[70]
    result = []
    for i in range(2, limit):
        if left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)