def all_pos_ints_inclusive(lst):
    if len(lst) < 52:
        return []
    return [i for i in lst[29:52] if i > 0]