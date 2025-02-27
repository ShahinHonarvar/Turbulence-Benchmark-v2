def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[175]
    res = []
    for i in range(2, x + 1):
        if not is_prime(i):
            continue
        str_i = str(i)
        if '0' in str_i:
            continue
        is_truncatable = True
        for j in range(1, len(str_i)):
            if not is_prime(int(str_i[j:])):
                is_truncatable = False
                break
        if is_truncatable:
            res.append(i)
    res.sort()
    return res