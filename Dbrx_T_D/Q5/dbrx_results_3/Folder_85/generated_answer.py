def all_neg_ints_inclusive(lst):
    if len(lst) < 9:
        return []
    return [i for i in lst[6:9] if i < 0]