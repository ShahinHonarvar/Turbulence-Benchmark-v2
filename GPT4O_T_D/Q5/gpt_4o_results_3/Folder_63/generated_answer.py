def all_neg_ints_inclusive(lst):
    if len(lst) < 23:
        return []
    return [x for x in lst[22:89] if x < 0]