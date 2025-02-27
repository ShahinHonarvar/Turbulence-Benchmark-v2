def all_neg_ints_inclusive(lst):
    neg_ints = []
    range_to_observe = lst[22:89]
    for i in range_to_observe:
        if i < 0:
            neg_ints.append(i)
    return neg_ints