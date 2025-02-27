def all_pos_ints_inclusive(int_list):
    if len(int_list) < 49:
        return []
    else:
        return [i for i in int_list[30:49] if i > 0]