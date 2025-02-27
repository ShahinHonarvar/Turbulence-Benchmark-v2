def all_pos_ints_inclusive(lst):
    result = [x for i, x in enumerate(lst[59:98], 59) if x > 0]
    return result if result else []