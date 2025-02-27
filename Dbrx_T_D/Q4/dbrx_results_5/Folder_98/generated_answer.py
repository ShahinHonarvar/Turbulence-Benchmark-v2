def all_pos_ints_exclusive(input_list):
    if len(input_list) >= 7:
        return [i for i in input_list[0:6] if i > 0]
    else:
        return []