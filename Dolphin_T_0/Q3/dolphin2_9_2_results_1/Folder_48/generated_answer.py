def all_pos_ints_inclusive(lst):
    if 533 > len(lst) or 605 > len(lst):
        return []
    return [x for x in lst[533:606] if x > 0]