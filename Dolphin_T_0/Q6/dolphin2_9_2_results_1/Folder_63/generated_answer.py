def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i in range(38, 53) if x < 0]