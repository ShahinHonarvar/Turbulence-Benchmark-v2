def all_pos_ints_exclusive(input_list):
    if len(input_list) < 49:
        return []
    pos_ints = [i for i in input_list[28:49] if i > 0]
    return pos_ints