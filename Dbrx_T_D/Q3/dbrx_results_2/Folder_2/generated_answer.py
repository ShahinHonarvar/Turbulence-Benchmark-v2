def all_pos_ints_inclusive(int_list):
    if len(int_list) < 40:
        return []
    else:
        return [i for i in int_list[14:40] if i > 0]