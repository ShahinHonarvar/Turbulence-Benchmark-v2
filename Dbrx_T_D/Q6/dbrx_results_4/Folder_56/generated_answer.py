def all_neg_ints_exclusive(lst):
    if len(lst) < 9:
        return []
    return [i for i in lst[7:9] if i < 0 and isinstance(i, int)]