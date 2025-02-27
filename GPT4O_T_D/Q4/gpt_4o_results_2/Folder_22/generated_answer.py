def all_pos_ints_exclusive(lst):
    if len(lst) <= 41:
        return []
    return [x for x in lst[41:200] if x > 0]