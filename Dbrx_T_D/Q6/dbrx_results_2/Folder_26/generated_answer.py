def all_neg_ints_exclusive(lst):
    if len(lst) < 78:
        return []
    return [i for i in lst[44:78] if i < 0]