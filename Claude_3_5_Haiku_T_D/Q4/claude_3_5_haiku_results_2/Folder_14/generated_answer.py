def all_pos_ints_exclusive(lst):
    if len(lst) <= 8:
        return []
    return [x for x in lst[2:7] if x > 0]