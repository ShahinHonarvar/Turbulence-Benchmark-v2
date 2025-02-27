def all_neg_ints_exclusive(lst):
    return [i for i in lst[0:5] if isinstance(i, int) and i < 0]