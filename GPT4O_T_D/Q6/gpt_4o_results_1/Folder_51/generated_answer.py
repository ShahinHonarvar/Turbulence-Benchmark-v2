def all_neg_ints_exclusive(lst):
    if len(lst) < 9:
        return []
    return [x for x in lst[7:9] if x < 0]