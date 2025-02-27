def all_ints_div_by_num(input_list):
    result = []
    for i in range(20, 201):
        if i >= len(input_list):
            break
        if input_list[i] % 4 == 0:
            result.append(input_list[i])
    return result