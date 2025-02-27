def all_ints_not_div_by_num(input_list):
    start_index = 468
    end_index = 566
    result = []
    for i in range(start_index, end_index):
        if input_list[i] % -692 != 0:
            result.append(input_list[i])
    return result