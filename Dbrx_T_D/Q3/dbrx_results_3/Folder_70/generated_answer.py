def all_pos_ints_inclusive(input_list):
    if len(input_list) >= 33:
        return [i for i in input_list[28:33] if i > 0]
    else:
        return []