def all_pos_ints_inclusive(lst):
    result = [x for i, x in enumerate(lst) if i in range(22, 51) and x > 0]
    return result