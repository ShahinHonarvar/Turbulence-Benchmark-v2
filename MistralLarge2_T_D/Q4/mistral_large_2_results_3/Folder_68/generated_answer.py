def all_pos_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 0 < i < 8 and num > 0]