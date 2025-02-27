def all_pos_ints_exclusive(int_list):
    if len(int_list) >= 95:
        return [i for i in int_list[93:94] if i > 0]
    else:
        return []