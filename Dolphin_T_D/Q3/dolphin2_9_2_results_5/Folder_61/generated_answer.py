def all_pos_ints_inclusive(lst):
    pos_ints = [num for num in lst[:8] if num > 0]
    return pos_ints if pos_ints else []