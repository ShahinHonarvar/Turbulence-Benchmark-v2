def all_ints_div_by_both_two_nums(input_list):
    result_list = []
    for i in range(2, 8):
        if input_list[i] % -1 == 0 and input_list[i] % -7 == 0:
            result_list.append(input_list[i])
    return result_list