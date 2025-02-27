def all_pos_ints_inclusive(int_list):
    if len(int_list) < 100:
        return []
    else:
        return [i for i in int_list[61:100] if i > 0]