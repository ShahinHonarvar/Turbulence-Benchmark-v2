def all_pos_ints_exclusive(input_list):
    return [input_list[i] for i in range(1, len(input_list) - 1) if input_list[i] > 0]