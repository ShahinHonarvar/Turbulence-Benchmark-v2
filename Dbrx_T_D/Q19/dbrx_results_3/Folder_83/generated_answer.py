def all_ints_not_div_by_num(input_list):
    start_index = 90
    end_index = 200
    output_list = [i for i in input_list[start_index:end_index] if i % -31 != 0]
    return output_list