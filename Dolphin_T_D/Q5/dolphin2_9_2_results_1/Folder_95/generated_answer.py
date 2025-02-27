def all_neg_ints_inclusive(lst):
    negs = []
    for i in range(82, 87):
        if lst[i] < 0:
            negs.append(lst[i])
    return negs