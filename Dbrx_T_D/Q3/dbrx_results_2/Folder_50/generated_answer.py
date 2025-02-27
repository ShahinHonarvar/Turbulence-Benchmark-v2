def all_pos_ints_inclusive(int_list):
    if len(int_list) >= 85:
        return [i for i in int_list[70:85] if i > 0]
    else:
        return []