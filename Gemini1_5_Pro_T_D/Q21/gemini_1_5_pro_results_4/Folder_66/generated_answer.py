def all_ints_div_by_num(input_list):
    result = []
    for i in range(max(14, 0), min(len(input_list), 69)):
        if input_list[i] % 18 == 0:
            result.append(input_list[i])
    return result