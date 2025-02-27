def all_ints_not_div_by_num(input_list):
    start_index = 8
    end_index = 9
    if end_index < len(input_list) and start_index < end_index:
        return [num for num in input_list[start_index:end_index] if num % 8 != 0]
    else:
        return []