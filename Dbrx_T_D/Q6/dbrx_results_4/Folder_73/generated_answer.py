def all_neg_ints_exclusive(lst):
    if len(lst) < 85:
        return []
    return [i for i in lst[36:85] if i < 0]