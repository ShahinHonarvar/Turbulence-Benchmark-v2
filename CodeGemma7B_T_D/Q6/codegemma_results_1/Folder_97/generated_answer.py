def all_neg_ints_exclusive(a):
    o = []
    for i in range(20, 93):
        if a[i] < 0 and i not in o:
            o.append(i)
    return o