def all_ints_div_by_num(input_list):
    start_index = 59
    end_index = 79
    result = [num for num in input_list[start_index:end_index + 1] if num % -82 == 0]
    return result