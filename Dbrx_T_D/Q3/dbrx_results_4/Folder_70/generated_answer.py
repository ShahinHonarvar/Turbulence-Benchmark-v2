def all_pos_ints_inclusive(int_list):
    if len(int_list) >= 33:
        return [i for i in int_list[28:33] if i > 0]
    else:
        return []