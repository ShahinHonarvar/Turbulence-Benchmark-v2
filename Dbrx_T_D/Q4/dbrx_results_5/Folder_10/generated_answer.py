def all_pos_ints_exclusive(input_list):
    if len(input_list) <= 74 or len(input_list) < 48:
        return []
    else:
        return [i for i in input_list[48:74] if i > 0]