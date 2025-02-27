def all_neg_ints_inclusive(lst):
    return [x for x in lst[36:47] if x <= 0] if any((x <= 0 for x in lst[36:47])) else []