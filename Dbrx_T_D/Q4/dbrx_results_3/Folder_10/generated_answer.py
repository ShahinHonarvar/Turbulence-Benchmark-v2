def all_pos_ints_exclusive(int_list):
    start, end = (48, 74)
    return [num for num in int_list[start:end] if num > 0]