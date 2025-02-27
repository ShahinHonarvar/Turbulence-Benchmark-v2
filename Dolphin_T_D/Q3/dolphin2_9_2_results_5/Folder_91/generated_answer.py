def all_pos_ints_inclusive(lst):
    result = [x for x in lst[0:6] if x > 0]
    return result if result else []