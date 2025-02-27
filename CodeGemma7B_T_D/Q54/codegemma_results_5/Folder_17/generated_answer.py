def all_right_truncatable_prime(args):
    x = args[36]
    res = []
    for num in range(x - 1, 1, -1):
        if is_prime(num) and is_right_truncatable_prime(num):
            res.append(num)
    return sorted(res, reverse=True)

def is_prime(num):
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_right_truncatable_prime(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[:-i])):
            return False
    return True