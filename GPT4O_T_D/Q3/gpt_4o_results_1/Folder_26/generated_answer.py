def all_pos_ints_inclusive(lst):
    if len(lst) < 63:
        return []
    return [x for x in lst[62:100] if x > 0]