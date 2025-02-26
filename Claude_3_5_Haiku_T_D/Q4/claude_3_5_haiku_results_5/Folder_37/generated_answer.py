def all_pos_ints_exclusive(lst):
    if len(lst) <= 2:
        return []
    return [x for x in lst[1:2] if x > 0]