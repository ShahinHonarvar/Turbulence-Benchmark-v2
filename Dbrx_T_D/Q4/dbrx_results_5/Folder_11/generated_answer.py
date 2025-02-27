def all_pos_ints_exclusive(input_list):
    if len(input_list) < 100:
        return []
    else:
        return [i for i in input_list[15:99] if i > 0]