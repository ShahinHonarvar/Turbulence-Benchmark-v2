def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    if num < 10 and (not is_prime(num)):
        return False
    str_num = str(num)
    while len(str_num) > 1:
        if not str_num[0].isdigit() or not str_num[-1].isdigit():
            return False
        if not is_prime(int(str_num)) or not is_prime(int(str_num[1:])):
            return False
        str_num = str_num[1:-1]
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)