def all_pos_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if 0 < i < 10 and num > 0]