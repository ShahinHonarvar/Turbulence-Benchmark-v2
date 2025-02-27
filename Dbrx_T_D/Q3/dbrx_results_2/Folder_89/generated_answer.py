def all_pos_ints_inclusive(input_list):
    if len(input_list) < 83:
        return []
    return [i for i in input_list[56:83] if i > 0]