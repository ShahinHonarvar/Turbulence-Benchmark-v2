def all_neg_ints_inclusive(lst):
    neg_ints = []
    for i in range(min(9, len(lst))):
        if lst[i] < 0:
            neg_ints.append(lst[i])
    return neg_ints