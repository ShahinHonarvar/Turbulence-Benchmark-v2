def all_ints_div_by_num(input_list):
    result = []
    for i in range(min(len(input_list), 3)):
        if input_list[i] % 5 == 0:
            result.append(input_list[i])
    return result