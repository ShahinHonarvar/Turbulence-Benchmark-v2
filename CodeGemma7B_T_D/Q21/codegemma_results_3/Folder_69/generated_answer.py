def all_ints_div_by_num(input_list):
    result = []
    for i in range(43, 77):
        if input_list[i] % 14 == 0:
            result.append(input_list[i])
    return result