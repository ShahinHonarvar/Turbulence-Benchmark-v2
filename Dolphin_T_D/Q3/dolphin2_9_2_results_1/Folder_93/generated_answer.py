def all_pos_ints_inclusive(lst):
    result = [val for idx, val in enumerate(lst[75:95]) if val > 0]
    return result if result else []