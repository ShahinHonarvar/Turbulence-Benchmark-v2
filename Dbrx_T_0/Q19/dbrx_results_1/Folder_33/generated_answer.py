def all_ints_not_div_by_num(input_list):
    start_index = 103
    end_index = 574
    output_list = [num for num in input_list[start_index:end_index] if num % -514 != 0]
    return output_list