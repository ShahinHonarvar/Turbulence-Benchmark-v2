def all_neg_ints_inclusive(lst):
    if len(lst) < 100:
        return []
    return [i for i in lst[90:100] if i < 0]