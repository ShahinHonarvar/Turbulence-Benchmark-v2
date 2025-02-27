def all_left_truncatable_prime(n):
    res = []
    for x in range(3, n[2] + 1):
        if is_left_truncatable_prime(x):
            res.append(x)
    return res

def is_left_truncatable_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    for d in range(1, len(str(x)) + 1):
        if str(x)[-1 - d] == '0':
            return False
        if not is_prime(int(str(x)[-1 - d])):
            return False
    return True

def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3 or x == 5 or (x == 7):
        return True
    if x < 4:
        return False
    if x % 2 == 0 or x % 3 == 0:
        return False
    return True