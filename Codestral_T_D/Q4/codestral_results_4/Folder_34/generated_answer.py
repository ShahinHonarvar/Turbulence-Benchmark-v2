def all_pos_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 60 < i < 200 and num > 0]