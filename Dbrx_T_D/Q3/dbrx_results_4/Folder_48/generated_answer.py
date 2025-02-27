def all_pos_ints_inclusive(lst):
    if len(lst) < 605:
        return []
    return [i for i in lst[533:606] if i > 0]