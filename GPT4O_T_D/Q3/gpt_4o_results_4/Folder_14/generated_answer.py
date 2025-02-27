def all_pos_ints_inclusive(lst):
    if len(lst) < 8:
        return []
    return [x for x in lst[5:8] if x > 0]