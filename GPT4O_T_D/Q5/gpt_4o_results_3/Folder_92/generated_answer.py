def all_neg_ints_inclusive(lst):
    if len(lst) < 2:
        return []
    return [i for i in lst[0:2] if i < 0]