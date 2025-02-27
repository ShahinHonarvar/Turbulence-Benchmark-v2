def all_ints_not_div_by_num(input_list):
    result = []
    for i in range(468, 566):
        if i < len(input_list) and input_list[i] % -692 != 0:
            result.append(input_list[i])
    return result