def all_pos_ints_inclusive(int_list):
    if len(int_list) < 98:
        return []
    else:
        return [i for i in int_list[21:98] if i > 0]