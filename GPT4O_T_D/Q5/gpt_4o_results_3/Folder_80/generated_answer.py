def all_neg_ints_inclusive(lst):
    if len(lst) < 67:
        return []
    return [x for x in lst[64:67] if x < 0]