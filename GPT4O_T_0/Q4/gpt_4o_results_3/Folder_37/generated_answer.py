def all_pos_ints_exclusive(lst):
    if len(lst) < 3:
        return []
    return [x for x in lst[2:-1] if x > 0]