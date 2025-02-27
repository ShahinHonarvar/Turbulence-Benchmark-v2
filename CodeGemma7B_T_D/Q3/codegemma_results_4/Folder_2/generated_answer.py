def all_pos_ints_inclusive(int_list):
    pos_ints = [i for i in int_list[15:39 + 1] if i > 0]
    return pos_ints if pos_ints else []