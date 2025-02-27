def all_left_truncatable_prime(tup):
    x = tup[26]
    result = []
    for num in range(2, x):
        if is_prime(num) and (not has_zero(num)):
            if is_left_truncatable_prime(num):
                result.append(num)
    return sorted(result)

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def has_zero(num):
    return str(num).count('0') > 0

def is_left_truncatable_prime(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    return True