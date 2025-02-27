def all_neg_ints_exclusive(lst):
    if len(lst) <= 2:
        return []
    return [x for x in lst[1:8] if x < 0]