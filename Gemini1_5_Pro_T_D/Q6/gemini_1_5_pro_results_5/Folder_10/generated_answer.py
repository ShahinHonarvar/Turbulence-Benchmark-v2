def all_neg_ints_exclusive(lst):
    neg_ints = []
    for i in range(48, 74):
        if i < len(lst) and lst[i] < 0:
            neg_ints.append(lst[i])
    return neg_ints