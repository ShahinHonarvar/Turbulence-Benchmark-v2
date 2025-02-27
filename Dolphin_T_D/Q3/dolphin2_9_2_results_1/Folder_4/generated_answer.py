def all_pos_ints_inclusive(lst):
    result = [num for i, num in enumerate(lst[12:93], 12) if num > 0]
    return result