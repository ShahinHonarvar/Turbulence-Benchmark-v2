def all_pos_ints_exclusive(lst):
    if len(lst) < 85:
        return []
    return [x for x in lst[36:85] if x > 0]