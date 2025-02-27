def all_pos_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i in range(59, 98) and x > 0]