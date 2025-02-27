def all_pos_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if 0 < idx < 6 and num > 0]