def all_neg_ints_exclusive(lst):
    if len(lst) < 80:
        return []
    return [i for i in lst[10:79] if i < 0]