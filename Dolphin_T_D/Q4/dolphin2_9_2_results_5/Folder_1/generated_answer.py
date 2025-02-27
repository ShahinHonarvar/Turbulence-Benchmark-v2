def all_pos_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i in range(66, 90) and x > 0]