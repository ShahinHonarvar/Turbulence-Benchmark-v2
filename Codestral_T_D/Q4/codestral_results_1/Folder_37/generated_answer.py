def all_pos_ints_exclusive(int_list):
    return [i for i in int_list[1:len(int_list) - 1] if i > 0]