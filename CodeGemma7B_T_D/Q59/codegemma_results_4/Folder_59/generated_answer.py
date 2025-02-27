def all_left_truncatable_prime(tup):
    x = tup[84]
    suml = set((str(i) for i in tup))
    for i in range(2, x):
        p = str(i)
        if '0' in p:
            continue
        las = set((p[j:] for j in range(len(p))))
        flag = True
        for j in las:
            if int(j) not in tup:
                flag = False
                break
        if flag:
            suml.add(p)
    return sorted(list(suml), reverse=True)