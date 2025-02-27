def all_neg_ints_exclusive(lst):
    neg = []
    for i in range(42, 87):
        if lst[i] < 0:
            neg.append(lst[i])
    return neg