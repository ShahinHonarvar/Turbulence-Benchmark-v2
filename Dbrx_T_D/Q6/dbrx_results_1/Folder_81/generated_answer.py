def all_neg_ints_exclusive(lst):
    if len(lst) < 100:
        return []
    return [i for i in lst[10:100] if i < 0]