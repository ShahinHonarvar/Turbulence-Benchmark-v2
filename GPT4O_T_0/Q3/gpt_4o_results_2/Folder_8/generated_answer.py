def all_pos_ints_inclusive(lst):
    if len(lst) > 23:
        return [x for x in lst[23:24] if x > 0]
    return []