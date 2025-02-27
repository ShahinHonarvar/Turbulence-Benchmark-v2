from math import sqrt

def all_right_truncatable_prime(tu):
    x = tu[11]
    li = []
    for i in range(2, x):
        if is_prime(i) and is_truncatable(i):
            li.append(i)
    return sorted(li)

def is_prime(num):
    if num <= 1:
        return False
    lim = int(sqrt(num)) + 1
    for i in range(2, lim):
        if num % i == 0:
            return False
    return True

def is_truncatable(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        trunc = int(str_num[:-i])
        if not is_prime(trunc):
            return False
    return True