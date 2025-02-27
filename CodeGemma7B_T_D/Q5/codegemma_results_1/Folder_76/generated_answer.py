def all_neg_ints_inclusive(lst):
    neg_ints = []
    for i in range(686, 988):
        if lst[i] < 0:
            neg_ints.append(lst[i])
    return neg_ints