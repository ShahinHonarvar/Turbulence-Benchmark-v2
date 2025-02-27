def all_pos_ints_exclusive(int_list):
    if len(int_list) < 35:
        return []
    else:
        return [i for i in int_list[27:34] if i > 0]