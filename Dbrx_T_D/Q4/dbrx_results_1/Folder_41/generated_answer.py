def all_pos_ints_exclusive(input_list):
    if len(input_list) >= 9 and input_list[8] > 0 and (input_list[7] > 0):
        return [num for num in input_list[8:9] if num > 0]
    else:
        return []