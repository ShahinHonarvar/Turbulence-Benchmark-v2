def all_pos_ints_exclusive(input_list):
    if len(input_list) < 9:
        return []
    else:
        return [i for i in input_list[3:8] if i > 0]