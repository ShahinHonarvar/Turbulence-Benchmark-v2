def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[39]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_right_truncatable_prime(num):
    str_num = str(num)
    while len(str_num) > 0:
        if not is_prime(int(str_num)):
            return False
        str_num = str_num[1:-1] if len(str_num) > 1 else ''
    return True