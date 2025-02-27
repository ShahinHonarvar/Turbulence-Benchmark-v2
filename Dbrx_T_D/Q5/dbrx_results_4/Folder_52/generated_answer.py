def all_neg_ints_inclusive(lst):
    if len(lst) < 39 or not isinstance(lst[0], int):
        return []
    return [i for i in lst[28:39] if i < 0]