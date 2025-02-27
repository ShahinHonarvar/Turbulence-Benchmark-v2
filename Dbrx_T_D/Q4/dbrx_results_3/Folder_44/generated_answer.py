def all_pos_ints_exclusive(input_list):
    if len(input_list) < 86:
        return []
    return [i for i in input_list[80:86] if i > 0]