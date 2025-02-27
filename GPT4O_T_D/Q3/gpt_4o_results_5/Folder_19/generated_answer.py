def all_pos_ints_inclusive(lst):
    if len(lst) < 6:
        return []
    return [x for x in lst[3:6] if x > 0]