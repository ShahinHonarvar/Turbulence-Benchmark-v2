def all_ints_div_by_num(input_list):
    result = []
    for i in range(max(13, len(input_list)) - min(len(input_list), 64), 13 - 1, -1):
        if input_list[i] % 46 == 0:
            result.append(input_list[i])
    return result