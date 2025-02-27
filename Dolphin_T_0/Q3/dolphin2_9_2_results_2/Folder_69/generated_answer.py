def all_pos_ints_inclusive(lst):
    result = [int_ for int_ in lst[32:36] if int_ > 0]
    return result if result else []