def all_pos_ints_exclusive(lst):
    result = [num for i, num in enumerate(lst) if num > 0 and 81 < i < 86]
    return result