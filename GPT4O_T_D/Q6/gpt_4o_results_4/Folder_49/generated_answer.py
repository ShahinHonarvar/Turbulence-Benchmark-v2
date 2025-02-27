def all_neg_ints_exclusive(lst):
    if len(lst) <= 81:
        return []
    return [x for x in lst[81:200] if x < 0]