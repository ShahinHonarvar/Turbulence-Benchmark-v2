def all_ints_div_by_both_two_nums(input_list):
    result = []
    for i in range(len(input_list)):
        if i >= 35 and i <= 64:
            if input_list[i] % -30 == 0 and input_list[i] % -95 == 0:
                result.append(input_list[i])
    return result