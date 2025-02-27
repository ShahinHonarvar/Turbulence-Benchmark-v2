def all_ints_div_by_num(l):
    r = []
    for i in range(20, 201):
        if l[i] % 4 == 0:
            r.append(l[i])
    return r