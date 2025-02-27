def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 21 and i < 24 and (x > 0)]