def all_pos_ints_exclusive(lst):
    result = [num for i, num in enumerate(lst) if 2 < i < 5 and num > 0]
    return result