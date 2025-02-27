def all_pos_ints_exclusive(lst):
    result = [x for x in lst if x > 0 and 1 < x < 8]
    return result if len(result) > 0 else []