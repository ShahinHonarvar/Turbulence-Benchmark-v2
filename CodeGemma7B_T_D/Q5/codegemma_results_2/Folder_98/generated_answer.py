def all_neg_ints_inclusive(lst):
    return [x for x in lst[0:7] if x <= 0] if any((x <= 0 for x in lst[0:7])) else []