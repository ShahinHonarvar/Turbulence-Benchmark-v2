def all_pos_ints_exclusive(int_list):
    if len(int_list) < 96:
        return []
    else:
        return [i for i in int_list[62:96] if i > 0]