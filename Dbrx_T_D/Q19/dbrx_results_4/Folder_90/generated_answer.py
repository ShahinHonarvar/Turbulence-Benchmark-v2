def all_ints_not_div_by_num(input_list):
    start_index = 767
    end_index = 905
    output_list = []
    for i in range(start_index, end_index):
        if input_list[i] % -430 != 0:
            output_list.append(input_list[i])
    return output_list