def all_neg_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[:9]) if x < 0]