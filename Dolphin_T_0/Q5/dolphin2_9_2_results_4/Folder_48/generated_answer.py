def all_neg_ints_inclusive(lst):
    if 605 < len(lst):
        return [x for x in lst[533:606] if x < 0]
    return []