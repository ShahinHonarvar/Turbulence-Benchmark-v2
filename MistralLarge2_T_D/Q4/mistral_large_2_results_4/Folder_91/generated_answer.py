def all_pos_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if num > 0 and 0 < i < 5]