def all_pos_ints_exclusive(input_list):
    if len(input_list) < 93:
        return []
    else:
        return [x for x in input_list[19:93] if x > 0]