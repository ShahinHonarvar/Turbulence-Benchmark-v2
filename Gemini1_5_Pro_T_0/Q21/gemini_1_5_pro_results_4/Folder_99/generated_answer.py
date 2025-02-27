def all_ints_div_by_num(input_list):
    result = []
    for i in range(max(161, len(input_list)), min(971, len(input_list))):
        if input_list[i] % 763 == 0:
            result.append(input_list[i])
    return result