def all_pos_ints_exclusive(int_list):
    pos_nums = [num for num in int_list if num > 0 and num < 5]
    return pos_nums or []