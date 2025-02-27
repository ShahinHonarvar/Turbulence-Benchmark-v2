def all_ints_not_div_by_num(input_list):
    result = []
    for i in range(50, 92):
        if input_list[i] % 16 != 0:
            result.append(input_list[i])
    return result