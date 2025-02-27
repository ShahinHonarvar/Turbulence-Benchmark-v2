def find_second_largest_num(input_list):
    input_list = sorted(input_list[533:606], reverse=True)
    return input_list[1] if len(input_list) > 1 else 'None'