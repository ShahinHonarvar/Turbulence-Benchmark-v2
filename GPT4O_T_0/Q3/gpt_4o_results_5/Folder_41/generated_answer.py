def all_pos_ints_inclusive(lst):
    if len(lst) > 6:
        return [x for x in lst[6:7] if x > 0]
    return []