def all_right_truncatable_prime(tu):
    x = tu[98]
    result = []
    for i in range(x // 2, 2, -1):
        if all((is_prime(i) and is_truncable(i, x) for j in range(1, i - 1))):
            result.append(i)
    return sorted(result)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncable(num, length):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    return True