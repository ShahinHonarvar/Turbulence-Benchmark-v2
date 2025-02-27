def all_right_truncatable_prime(tup):
    x = tup[618]
    res = []
    for i in range(2, x):
        if is_prime(i):
            if is_right_truncatable(i):
                res.append(i)
    return sorted(res)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_right_truncatable(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[:-i])):
            return False
    return True