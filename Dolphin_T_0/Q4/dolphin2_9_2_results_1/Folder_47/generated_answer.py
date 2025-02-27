def all_pos_ints_exclusive(lst):
    result = [x for i, x in enumerate(lst) if i > 63 and i < 80 and (x > 0)]
    return result