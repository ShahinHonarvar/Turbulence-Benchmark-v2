def all_pos_ints_inclusive(ints):
    result = [i for i in ints[32:36] if i > 0]
    return result if result else []