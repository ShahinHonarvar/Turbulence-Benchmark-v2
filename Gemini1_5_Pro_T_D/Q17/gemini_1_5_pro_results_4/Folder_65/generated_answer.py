def all_ints_div_by_both_two_nums(input_list):
    output_list = []
    for i in range(50, 93):
        if i in range(len(input_list)):
            if input_list[i] % -94 == 0 and input_list[i] % -95 == 0:
                output_list.append(input_list[i])
    return output_list