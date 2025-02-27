def all_pos_ints_exclusive(lst):
    return [i for i in lst[1] if isinstance(i, int) and i > 0]