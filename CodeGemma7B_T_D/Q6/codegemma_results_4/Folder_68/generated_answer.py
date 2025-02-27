def all_neg_ints_exclusive(lst):
    if not any((n in lst for n in range(-8, 0))):
        return []
    return [x for x in lst if x in range(-8, 0) and x not in range(0, 9)]