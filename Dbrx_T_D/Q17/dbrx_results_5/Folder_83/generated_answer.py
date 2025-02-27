def all_ints_div_by_both_two_nums(input_list):
    output_list = []
    for i in range(90, 201):
        if input_list[i] % -31 == 0 and input_list[i] % 13 == 0:
            output_list.append(input_list[i])
    return output_list