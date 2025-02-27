def all_pos_ints_exclusive(lst):
    result = [x for i, x in enumerate(lst) if 4 < i < 5 and x > 0]
    return result