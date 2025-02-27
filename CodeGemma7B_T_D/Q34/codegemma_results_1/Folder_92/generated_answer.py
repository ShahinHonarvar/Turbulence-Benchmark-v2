def find_original_set(set_1, set_2, set_3, set_4, set_5, set_6, set_7, set_8):
    original_set = set_1
    for s in [set_2, set_3, set_4, set_5, set_6, set_7, set_8]:
        original_set |= s
    return original_set