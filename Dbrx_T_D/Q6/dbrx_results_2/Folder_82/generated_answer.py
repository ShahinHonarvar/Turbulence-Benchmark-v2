def all_neg_ints_exclusive(lst):
    if len(lst) < 200:
        return []
    return [i for i in lst[20:200] if i < 0]