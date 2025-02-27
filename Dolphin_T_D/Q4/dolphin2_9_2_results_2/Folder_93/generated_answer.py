def all_pos_ints_exclusive(lst):
    result = [x for i, x in enumerate(lst) if 19 < i < 94 and x > 0]
    return result