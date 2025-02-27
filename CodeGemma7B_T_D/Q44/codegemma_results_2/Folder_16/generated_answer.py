def composite_nums_between_indices(l):
    res = set()
    for i in range(40, 81):
        if l[i] != 1 and l[i] != 2:
            j = 2
            flag = False
            while j <= l[i] // 2:
                if l[i] % j == 0:
                    flag = True
                    break
                j += 1
            if flag:
                res.add(l[i])
    return res