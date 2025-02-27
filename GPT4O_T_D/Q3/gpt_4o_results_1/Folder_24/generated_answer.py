def all_pos_ints_inclusive(int_list):
    if len(int_list) < 96:
        return []
    return [x for x in int_list[74:96] if x > 0]