def all_neg_ints_exclusive(lst):
    if len(lst) < 3:
        return []
    return [x for x in lst[1:2] if x < 0]