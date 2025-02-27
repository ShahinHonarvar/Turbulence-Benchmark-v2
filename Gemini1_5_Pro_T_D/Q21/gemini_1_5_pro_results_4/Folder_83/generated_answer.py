def all_ints_div_by_num(input_list):
    result = []
    for i in range(40, 401):
        if i < len(input_list) and input_list[i] % 7 == 0:
            result.append(input_list[i])
    return result