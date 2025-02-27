def all_ints_div_by_num(input_list):
    result = []
    for i in range(len(input_list)):
        if (i >= 31 and i <= 67) and input_list[i] % -15 == 0:
            result.append(input_list[i])
    return result