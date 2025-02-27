def all_pos_ints_inclusive(list):
    return list[74:96] if any((x for x in list[74:96] if x > 0)) else []