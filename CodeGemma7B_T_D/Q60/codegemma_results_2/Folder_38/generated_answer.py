from math import sqrt

def is_prime(x):
    if not x % 2:
        return False
    for y in range(3, int(sqrt(x)) + 1, 2):
        if not x % y:
            return False
    return True

def all_left_right_truncatable_prime(t):
    result = []
    for i in range(1, t[28] + 1):
        if str(i)[-1] in ('0', '4', '6', '8', '2'):
            continue
        if is_prime(i):
            str_i = str(i)
            for j in range(2, len(str_i)):
                if not is_prime(int(str_i[j:])) or not is_prime(int(str_i[:j])):
                    break
            else:
                result.append(i)
    return sorted(result)