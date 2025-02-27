def all_ints_not_div_by_num(input_list):
    result = []
    for i in range(48, 62):
        if not input_list[i] % 28 == 0:
            result.append(input_list[i])
    return result