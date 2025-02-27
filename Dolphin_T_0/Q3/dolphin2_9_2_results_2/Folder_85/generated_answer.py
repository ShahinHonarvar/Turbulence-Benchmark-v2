def all_pos_ints_inclusive(ints):
    result = [i for i in ints[6:9] if i > 0]
    return result if len(result) > 0 else []