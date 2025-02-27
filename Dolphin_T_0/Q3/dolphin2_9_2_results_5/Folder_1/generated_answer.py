def all_pos_ints_inclusive(lst):
    result = [x for i, x in enumerate(lst) if i in range(31, 73) and x > 0]
    return result if result else []