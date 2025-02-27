def all_neg_ints_exclusive(lst):
    if len(lst) < 97:
        return []
    return [i for i in lst[69:97] if i < 0]