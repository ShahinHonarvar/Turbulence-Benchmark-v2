def all_pos_ints_inclusive(lst):
    result = [x for x in lst[52:72] if x > 0]
    return result if len(result) > 0 else []