def all_neg_ints_inclusive(lst):
    if len(lst) < 6:
        return []
    return [i for i in lst[3:6] if i < 0]