def all_ints_div_by_num(input_list):
    result = []
    for i in range(max(30, len(input_list)), 60):
        if i < len(input_list) and input_list[i] % 39 == 0:
            result.append(input_list[i])
    return result