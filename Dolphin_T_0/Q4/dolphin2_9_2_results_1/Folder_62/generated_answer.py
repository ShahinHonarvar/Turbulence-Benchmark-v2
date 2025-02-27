def all_pos_ints_exclusive(lst):
    result = [x for i, x in enumerate(lst) if 55 < i < 84 and x > 0]
    return result if result else []