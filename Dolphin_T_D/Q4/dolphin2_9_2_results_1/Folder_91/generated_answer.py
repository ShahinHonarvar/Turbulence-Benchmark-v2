def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 0 and i < 5 and (x > 0)]