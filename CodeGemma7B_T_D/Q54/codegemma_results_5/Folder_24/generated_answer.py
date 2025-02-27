def all_right_truncatable_prime(t):
    x = t[65]
    prime_list = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    res = []
    for p in prime_list:
        if p >= x:
            continue
        elif has_right_truncatable_flag(prime_list, p):
            res.append(p)
    res = sorted(res, reverse=True)
    return res

def has_right_truncatable_flag(prime_list, p):
    tmp = str(p)
    for i in range(1, len(tmp)):
        if int(tmp[:-i]) in prime_list:
            continue
        else:
            return False
    return True