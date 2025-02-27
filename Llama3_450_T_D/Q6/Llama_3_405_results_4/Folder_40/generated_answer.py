def all_neg_ints_exclusive(lst):
    return [i for i in lst[1:3] if isinstance(i, int) and i < 0]