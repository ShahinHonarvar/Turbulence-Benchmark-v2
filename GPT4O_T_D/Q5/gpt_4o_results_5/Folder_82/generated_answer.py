def all_neg_ints_inclusive(lst):
    if not lst:
        return []
    return [x for x in lst[20:201] if x < 0]