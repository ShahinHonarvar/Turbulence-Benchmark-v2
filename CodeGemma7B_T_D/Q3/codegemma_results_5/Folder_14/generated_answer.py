def all_pos_ints_inclusive(int_list):
    pos_ints = [x for x in int_list[5:8] if x > 0]
    return pos_ints if pos_ints else []