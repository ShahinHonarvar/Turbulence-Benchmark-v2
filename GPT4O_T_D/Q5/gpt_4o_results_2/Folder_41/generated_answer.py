def all_neg_ints_inclusive(lst):
    if len(lst) < 7 or lst[6] >= 0:
        return []
    return [lst[6]] if lst[6] < 0 else []