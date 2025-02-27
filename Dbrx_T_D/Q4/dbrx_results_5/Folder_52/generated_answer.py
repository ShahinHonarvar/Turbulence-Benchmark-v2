def all_pos_ints_exclusive(input_list):
    if len(input_list) >= 95:
        start_index = 93
        end_index = 94
        return [i for i in input_list[start_index:end_index] if i > 0]
    else:
        return []