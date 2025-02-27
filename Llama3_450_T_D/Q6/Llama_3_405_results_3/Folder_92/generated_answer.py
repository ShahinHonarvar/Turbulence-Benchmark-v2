def all_neg_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[1:-1]) if x < 0]