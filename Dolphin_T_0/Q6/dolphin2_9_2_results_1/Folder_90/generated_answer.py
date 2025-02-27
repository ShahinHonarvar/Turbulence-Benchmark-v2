def all_neg_ints_exclusive(lst):
    sublist = lst[389:748]
    neg_ints = [item for item in sublist if item < 0]
    return neg_ints