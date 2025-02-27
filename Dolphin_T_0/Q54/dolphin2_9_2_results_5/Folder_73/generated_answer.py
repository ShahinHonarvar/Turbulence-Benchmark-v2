import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_right_truncatable(num):
    while len(str(num)) > 1:
        if not is_prime(num):
            return False
        num = int(str(num)[:-1])
    return True

def all_right_truncatable_prime(tup):
    x = tup[97]
    ret = [i for i in range(x) if is_right_truncatable(i) and is_prime(i)]
    return sorted(ret)