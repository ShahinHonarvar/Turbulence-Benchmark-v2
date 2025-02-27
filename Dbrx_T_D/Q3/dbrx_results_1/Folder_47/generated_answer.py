def all_pos_ints_inclusive(input_list):
    if len(input_list) < 77:
        return []
    return [i for i in input_list[36:77] if i > 0]