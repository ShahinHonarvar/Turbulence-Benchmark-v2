from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def left_truncatable(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])) or '0' in str_num[i:]:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[79]
    return sorted([num for num in range(x) if left_truncatable(num)], reverse=True)