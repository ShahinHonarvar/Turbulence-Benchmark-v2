def all_pos_ints_exclusive(lst):
    if len(lst) < 85 or 55 > len(lst):
        return []
    return [i for i in lst[55:84] if i > 0]