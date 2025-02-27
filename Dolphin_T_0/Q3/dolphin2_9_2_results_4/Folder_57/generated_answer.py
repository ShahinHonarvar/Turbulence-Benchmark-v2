def all_pos_ints_inclusive(int_list):
    if len(int_list) < 56:
        return []
    else:
        return [i for i in int_list[27:56] if i > 0]