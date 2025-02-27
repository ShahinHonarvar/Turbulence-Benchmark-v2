def all_pos_ints_exclusive(input_list):
    if len(input_list) < 8:
        return []
    else:
        return [num for num in input_list[2:8] if num > 0]