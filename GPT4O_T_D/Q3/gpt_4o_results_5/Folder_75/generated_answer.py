def all_pos_ints_inclusive(lst):
    if len(lst) < 58:
        return []
    return [x for x in lst[56:58] if x > 0]