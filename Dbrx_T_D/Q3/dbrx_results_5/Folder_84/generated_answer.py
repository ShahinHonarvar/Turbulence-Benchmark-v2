def all_pos_ints_inclusive(input_list):
    if len(input_list) < 86:
        return []
    elif len(input_list) == 86:
        return [i for i in input_list if i > 0]
    else:
        pos_ints = [i for i in input_list[43:87] if i > 0]
        return pos_ints