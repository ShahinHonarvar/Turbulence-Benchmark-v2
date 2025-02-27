def all_pos_ints_exclusive(int_list):
    return [i for i in range(0, 11) if i > 0 and i < len(int_list) and (int_list[i] > 0)]