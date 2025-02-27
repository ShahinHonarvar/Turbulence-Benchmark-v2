import math

def all_left_right_truncatable_prime(x):
    res = []
    for num in range(2, x + 1):
        if not num % 2 and num != 2:
            continue
        if not all((int(i) for i in str(num))):
            continue
        if is_prime(num):
            if is_truncatable(num):
                res.append(num)
    if not res:
        return []
    return sorted(res)

def is_prime(num):
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if not num % i:
            return False
    return True

def is_truncatable(num):
    num = str(num)
    for i in range(1, len(num)):
        if not is_prime(int(num[i:])):
            return False
        if not is_prime(int(num[:-i])):
            return False
    return True