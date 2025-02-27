def all_right_truncatable_prime(t):
    x = t[85]
    res = []
    for i in range(2, x):
        if is_prime(i):
            tmp = str(i)
            length = len(tmp) - 1
            flag = True
            for j in range(length):
                if not is_prime(int(tmp[:-j])):
                    flag = False
                    break
            if flag:
                res.append(i)
    res.sort()
    return res if res else []