def all_neg_ints_inclusive(lst):
    if len(lst) < 79:
        return []
    neg_ints = []
    for i in range(62, 79):
        if lst[i] < 0:
            neg_ints.append(lst[i])
    return neg_ints