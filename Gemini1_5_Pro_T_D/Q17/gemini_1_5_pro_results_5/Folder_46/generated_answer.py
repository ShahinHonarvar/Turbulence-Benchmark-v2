def all_ints_div_by_both_two_nums(input_list):
    output_list = []
    for i in range(11, 47):
        if i < len(input_list) and input_list[i] % 55 == 0 and (input_list[i] % 36 == 0):
            output_list.append(input_list[i])
    return output_list