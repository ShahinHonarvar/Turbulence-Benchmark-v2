def all_ints_not_div_by_num(input_list):
    output_list = []
    for i in range(len(input_list)):
        if i >= 45 and i < 72:
            if input_list[i] % 93 != 0:
                output_list.append(input_list[i])
    return output_list