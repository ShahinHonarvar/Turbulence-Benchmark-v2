def all_pos_ints_inclusive(int_list):
    if len(int_list) > 6:
        return [x for x in int_list[6:7] if x > 0]
    return []