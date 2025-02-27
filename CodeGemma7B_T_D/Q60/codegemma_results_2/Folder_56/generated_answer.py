from math import sqrt

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def truncate(num):
    dig_as_list = list(str(num))
    res = set()
    for i in range(1, len(dig_as_list)):
        res.add(int(''.join(dig_as_list[i:])))
        res.add(int(''.join(dig_as_list[:-i])))
    return res

def is_left_right_truncatable_prime(num):
    if not is_prime(num):
        return False
    if '0' in str(num):
        return False
    return all((is_prime(x) for x in truncate(num)))

def all_left_right_truncatable_prime(x):
    res = []
    for i in range(x + 1):
        if is_left_right_truncatable_prime(i):
            res.append(i)
    return sorted(res)