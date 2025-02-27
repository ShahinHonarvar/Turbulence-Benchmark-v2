def all_ints_not_div_by_num(input_list):
    start_index = 103
    end_index = 574
    output_list = []
    for i in range(len(input_list)):
        if i >= start_index and i < end_index and (input_list[i] % -514 != 0):
            output_list.append(input_list[i])
    return output_list