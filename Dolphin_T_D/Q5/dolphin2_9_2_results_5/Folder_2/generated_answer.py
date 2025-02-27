def all_neg_ints_inclusive(lst):
    if 15 <= 39 < len(lst):
        return [val for val in lst[15:39] if val < 0]
    else:
        return []