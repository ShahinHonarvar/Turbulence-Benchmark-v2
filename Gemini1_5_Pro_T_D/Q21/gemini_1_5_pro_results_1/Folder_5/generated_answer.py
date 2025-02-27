def all_ints_div_by_num(input_list):
    output_list = []
    for i in range(1, 5):
        if i < len(input_list) and input_list[i] % -6 == 0:
            output_list.append(input_list[i])
    return output_list