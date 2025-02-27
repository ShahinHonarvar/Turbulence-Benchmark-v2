def all_pos_ints_inclusive(int_list):
    if len(int_list) < 70:
        return []
    else:
        return [i for i in int_list[70:85] if i > 0]