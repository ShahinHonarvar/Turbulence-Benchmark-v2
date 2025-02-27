def all_ints_not_div_by_num(input_list):
    if len(input_list) < 5:
        return []
    start_index = 2
    end_index = start_index + 3
    result = [num for num in input_list[start_index:end_index] if num % 2 != 0]
    if len(result) == 0:
        return []
    return result