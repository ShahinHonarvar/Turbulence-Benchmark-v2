def all_neg_ints_inclusive(lst):
    if len(lst) < 24:
        return []
    if lst[23] < 0:
        return [lst[23]]
    return []