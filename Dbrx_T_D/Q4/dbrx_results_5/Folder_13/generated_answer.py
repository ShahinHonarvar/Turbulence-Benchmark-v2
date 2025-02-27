def all_pos_ints_exclusive(lst):
    if len(lst) < 85 or 73 > len(lst):
        return []
    return [i for i in lst[73:84] if i > 0]