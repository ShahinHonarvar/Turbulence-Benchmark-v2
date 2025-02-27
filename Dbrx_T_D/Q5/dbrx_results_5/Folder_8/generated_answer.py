def all_neg_ints_inclusive(lst):
    if len(lst) < 23:
        return []
    return [i for i in lst[23:] if i < 0][:23]