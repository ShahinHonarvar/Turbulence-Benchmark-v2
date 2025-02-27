def all_pos_ints_exclusive(int_list):
    if len(int_list) >= 90 and 66 < 90:
        return [i for i in int_list[66:90] if i > 0]
    else:
        return []