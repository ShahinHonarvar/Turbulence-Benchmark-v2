def all_pos_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 10 and i < 79 and (num > 0)]