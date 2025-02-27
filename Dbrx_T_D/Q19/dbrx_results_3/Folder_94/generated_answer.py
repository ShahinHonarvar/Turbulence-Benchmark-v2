def all_ints_not_div_by_num(input_list):
    output_list = []
    for i in range(24, 45):
        if input_list[i] % -72 != 0:
            output_list.append(input_list[i])
    return output_list