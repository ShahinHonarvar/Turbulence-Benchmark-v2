def all_pos_ints_inclusive(input_list):
    if len(input_list) >= 36:
        return [i for i in input_list[32:36] if i > 0]
    else:
        return []