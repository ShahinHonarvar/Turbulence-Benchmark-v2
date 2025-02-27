def all_left_truncatable_prime(tupl):
    x = tupl[835]
    results = []
    for v in range(x):
        li = list(map(int, str(v)))
        flag = True
        if 0 in li:
            continue
        for a in range(len(li)):
            tmp = ''.join(map(str, li[a:]))
            d = int(tmp)
            if d <= 1:
                flag = False
                break
            elif d != 2 and d % 2 == 0 or (d != 5 and d % 5 == 0):
                flag = False
                break
        if flag:
            results.append(v)
    results.sort()
    return results