def all_neg_ints_inclusive(lst):
    if len(lst) < 97:
        return []
    return [i for i in lst[59:98] if i < 0]