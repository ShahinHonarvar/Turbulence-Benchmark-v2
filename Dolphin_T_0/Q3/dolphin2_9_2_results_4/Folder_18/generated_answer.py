def all_pos_ints_inclusive(lst):
    result = [value for i, value in enumerate(lst[35:50]) if value > 0]
    return result if result else []