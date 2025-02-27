def all_pos_ints_inclusive(input_list):
    if 4 <= len(input_list) >= 8:
        return [i for i in input_list[4:9] if i > 0]
    else:
        return []