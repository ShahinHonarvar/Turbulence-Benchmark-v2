def all_pos_ints_inclusive(int_list):
    if len(int_list) < 99:
        return []
    return [i for i in int_list[90:100] if i > 0]