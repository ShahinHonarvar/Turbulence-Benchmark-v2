def all_pos_ints_inclusive(lst):
    if len(lst) <= 76:
        return []
    return [x for x in lst[37:77] if x > 0]