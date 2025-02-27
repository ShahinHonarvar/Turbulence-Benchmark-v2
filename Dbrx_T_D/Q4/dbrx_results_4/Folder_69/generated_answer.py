def all_pos_ints_exclusive(int_list):
    if len(int_list) < 99:
        return []
    return [i for i in int_list[68:99] if i > 0]