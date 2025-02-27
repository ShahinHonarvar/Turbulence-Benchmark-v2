def all_neg_ints_inclusive(lst):
    if len(lst) < 99:
        return []
    return [i for i in lst[55:99] if i < 0]