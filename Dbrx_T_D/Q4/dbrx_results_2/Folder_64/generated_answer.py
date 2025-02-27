def all_pos_ints_exclusive(input_list):
    if len(input_list) < 4:
        return []
    return [x for x in input_list[0:4] if x > 0]