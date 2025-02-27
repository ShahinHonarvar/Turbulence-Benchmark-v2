def all_ints_not_div_by_num(input_list):
    output_list = []
    for i in range(43, 77):
        if i >= len(input_list):
            break
        if input_list[i] % 84 != 0:
            output_list.append(input_list[i])
    return output_list