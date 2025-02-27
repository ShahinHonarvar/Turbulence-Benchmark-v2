def all_pos_ints_inclusive(int_list):
    if len(int_list) < 27:
        return []
    return [x for x in int_list[26:53] if x > 0]