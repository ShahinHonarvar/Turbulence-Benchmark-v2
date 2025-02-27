def all_neg_ints_inclusive(lst):
    if len(lst) < 31:
        return []
    else:
        return [i for i in lst[20:31] if i < 0]