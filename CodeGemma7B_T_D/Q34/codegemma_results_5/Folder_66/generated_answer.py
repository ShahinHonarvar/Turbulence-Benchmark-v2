def find_original_set(set_1, set_2, set_3, set_4, set_5, set_6, set_7, set_8, set_9, set_10, set_11, set_12, set_13, set_14, set_15, set_16, set_17, set_18, set_19, set_20, set_21, set_22, set_23, set_24, set_25):
    original_set = set_1
    for sets in (set_2, set_3, set_4, set_5, set_6, set_7, set_8, set_9, set_10, set_11, set_12, set_13, set_14, set_15, set_16, set_17, set_18, set_19, set_20, set_21, set_22, set_23, set_24, set_25):
        original_set = original_set.union(sets)
    return original_set