def all_pos_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 23 < i < 45 and isinstance(num, int) and (num > 0)]