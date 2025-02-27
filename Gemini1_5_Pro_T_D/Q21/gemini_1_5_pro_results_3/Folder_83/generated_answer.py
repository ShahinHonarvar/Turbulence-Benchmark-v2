def all_ints_div_by_num(input_list):
    result = []
    for i in range(max(0, min(len(input_list) - 1, 40)), min(len(input_list), 401)):
        if input_list[i] % 7 == 0:
            result.append(input_list[i])
    return result