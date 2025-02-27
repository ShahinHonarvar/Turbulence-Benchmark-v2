def all_ints_div_by_num(input_list):
    result = []
    for i in range(max(87, 0), min(90, len(input_list))):
        if input_list[i] % 55 == 0:
            result.append(input_list[i])
    return result