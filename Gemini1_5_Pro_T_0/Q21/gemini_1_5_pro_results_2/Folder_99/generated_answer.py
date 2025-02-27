def all_ints_div_by_num(input_list):
    result = []
    for i in range(161, 971):
        if i < len(input_list) and input_list[i] % 763 == 0:
            result.append(input_list[i])
    return result