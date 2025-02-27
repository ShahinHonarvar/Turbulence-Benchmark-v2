def all_pos_ints_exclusive(input_list):
    if len(input_list) < 8:
        return []
    return [x for x in input_list[8:9] if x > 0]