def all_neg_ints_inclusive(lst):
    if len(lst) < 64:
        return []
    return [i for i in lst[14:65] if i < 0]