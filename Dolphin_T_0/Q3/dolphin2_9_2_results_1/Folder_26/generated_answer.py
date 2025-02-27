def all_pos_ints_inclusive(lst):
    result = [num for i, num in enumerate(lst[62:100], 62) if num > 0]
    return result