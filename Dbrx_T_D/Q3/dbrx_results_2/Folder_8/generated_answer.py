def all_pos_ints_inclusive(int_list):
    if len(int_list) < 23:
        return []
    return [i for i in int_list[22:23 + 1] if i > 0]