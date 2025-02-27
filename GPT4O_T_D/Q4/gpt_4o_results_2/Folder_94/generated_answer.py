def all_pos_ints_exclusive(lst):
    if len(lst) <= 28:
        return []
    return [x for x in lst[29:53] if x > 0]