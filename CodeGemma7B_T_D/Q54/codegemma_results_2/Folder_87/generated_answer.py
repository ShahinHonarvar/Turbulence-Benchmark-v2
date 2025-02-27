import math

def all_right_truncatable_prime(tp):
    x = tp[39]
    ret = []
    for i in range(2, x):
        if is_prime(i) and is_prime_truncatable(str(i)):
            ret.append(i)
    return sorted(ret, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_prime_truncatable(num):
    num = str(num)
    for i in range(1, len(num)):
        if not is_prime(int(num[:-i])):
            return False
    return True