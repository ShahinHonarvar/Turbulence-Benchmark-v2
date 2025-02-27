def all_pos_ints_inclusive(lst):
    sublist = lst[30:201]
    pos_ints = [num for num in sublist if num > 0]
    return pos_ints if pos_ints else []