def all_ints_not_div_by_num(input_list):
    if len(input_list) < 574:
        return []
    output_list = []
    for i in range(103, 574):
        if input_list[i] % -514 != 0:
            output_list.append(input_list[i])
    return output_list