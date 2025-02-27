def all_pos_ints_inclusive(int_list):
    result = [x for x in int_list[4:9] if x > 0]
    return result if len(result) > 0 else []