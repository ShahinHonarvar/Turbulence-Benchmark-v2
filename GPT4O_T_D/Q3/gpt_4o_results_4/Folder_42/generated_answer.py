def all_pos_ints_inclusive(lst):
    if len(lst) < 30:
        return []
    return [i for i in lst[29:80] if i > 0]