def all_pos_ints_inclusive(lst):
    if len(lst) <= 605:
        return []
    positive_slice = [x for x in lst[533:606] if x > 0]
    return positive_slice