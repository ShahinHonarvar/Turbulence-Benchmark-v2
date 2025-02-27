def all_pos_ints_inclusive(input_list):
    if not input_list or max(input_list) < 1 or min(input_list) > 7:
        return []
    return list(range(1, 8))