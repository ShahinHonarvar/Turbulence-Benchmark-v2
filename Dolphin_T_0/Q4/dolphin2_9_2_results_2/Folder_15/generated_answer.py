def all_pos_ints_exclusive(lst):
    return [v for i, v in enumerate(lst) if 1 <= i < len(lst) - 1 and v > 0]