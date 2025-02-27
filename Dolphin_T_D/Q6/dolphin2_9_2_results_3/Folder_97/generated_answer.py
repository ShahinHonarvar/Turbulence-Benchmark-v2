def all_neg_ints_exclusive(lst):
    result = [x for i, x in enumerate(lst) if 20 < i < 93 and x < 0]
    return result