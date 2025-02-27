def all_pos_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if 15 < idx < 99 and num > 0]