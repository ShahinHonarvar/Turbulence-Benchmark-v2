def all_pos_ints_inclusive(int_list):
    if len(int_list) < 41 or int_list[27] > 0:
        return []
    return [x for x in int_list[27:41] if x > 0]