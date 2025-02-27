def all_pos_ints_inclusive(input_list):
    if len(input_list) >= 67:
        return [i for i in input_list[64:67] if i > 0]
    else:
        return []