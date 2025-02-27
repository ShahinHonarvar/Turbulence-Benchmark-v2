from math import sqrt

def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x <= 1:
        return False
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    return True

def right_truncatable_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if not is_prime(int(str_num[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[39]
    result = []
    for i in range(2, x + 1):
        if str(i).find('0') == -1 and left_truncatable_prime(i) and right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True) or []