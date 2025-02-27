def all_neg_ints_inclusive(lst):
    if len(lst) < 71:
        return []
    return [x for x in lst[70:201] if x < 0]