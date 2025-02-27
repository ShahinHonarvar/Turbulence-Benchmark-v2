def all_pos_ints_inclusive(lst):
    return [num for idx, num in enumerate(lst) if num > 0 and idx <= 10]