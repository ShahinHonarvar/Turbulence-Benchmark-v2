def all_pos_ints_exclusive(ints):
    result = [i for i in ints[22:24] if i > 0]
    return result if len(result) > 0 else []