def all_pos_ints_inclusive(lst):
    if len(lst) < 24:
        return []
    result = [x for x in lst[23:24] if x > 0]
    return result