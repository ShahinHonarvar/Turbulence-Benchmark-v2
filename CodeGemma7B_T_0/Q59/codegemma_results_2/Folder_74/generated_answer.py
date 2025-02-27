def all_left_truncatable_prime(tup):
    x = tup[36]
    result = []
    for i in range(2, x):
        if is_prime(i) and (not has_zero(i)):
            if is_left_truncatable(i):
                result.append(i)
    return sorted(result)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def has_zero(num):
    return '0' in str(num)

def is_left_truncatable(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    return True