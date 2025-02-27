def all_pos_ints_exclusive(int_list):
    return [int_list[i] for i in range(1, len(int_list) - 1) if int_list[i] > 0]