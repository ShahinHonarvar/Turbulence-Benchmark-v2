def all_neg_ints_inclusive(a):
    t = []
    for i in range(43, 87):
        if a[i] < 0:
            t.append(a[i])
    return t