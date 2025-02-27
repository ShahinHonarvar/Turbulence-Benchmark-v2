def all_pos_ints_exclusive(lst):
    if len(lst) <= 21:
        return []
    return [i for i in lst[21:200] if i > 0]