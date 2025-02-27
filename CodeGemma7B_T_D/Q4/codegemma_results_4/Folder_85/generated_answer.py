def all_pos_ints_exclusive(lst):
    pos_ints = [num for num in lst[4:5] if num > 0]
    return pos_ints if pos_ints else []