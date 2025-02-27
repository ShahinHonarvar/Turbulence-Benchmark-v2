def all_ints_div_by_both_two_nums(input_list):
    result = []
    for i in range(7):
        if i < len(input_list):
            if input_list[i] % -5 == 0 and input_list[i] % -6 == 0:
                result.append(input_list[i])
    return result