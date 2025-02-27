def all_pos_ints_exclusive(lst):
    if len(lst) <= 33:
        return []
    return [x for x in lst[33:99] if x > 0]