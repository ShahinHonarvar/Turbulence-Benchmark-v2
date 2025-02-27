def all_pos_ints_exclusive(lst):
    if len(lst) < 53:
        return []
    return [x for x in lst[39:52] if x > 0]