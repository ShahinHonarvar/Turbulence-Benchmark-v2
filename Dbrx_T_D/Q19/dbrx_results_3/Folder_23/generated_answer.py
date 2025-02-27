def all_ints_not_div_by_num(input_list):
    start_index = 44
    end_index = 91
    output_list = [i for i in input_list[start_index:end_index] if i % -68 != 0]
    return output_list