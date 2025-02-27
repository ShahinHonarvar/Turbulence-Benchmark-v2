def all_pos_ints_exclusive(lst):
    if len(lst) <= 29:
        return []
    return [x for x in lst[29:49] if x > 0]