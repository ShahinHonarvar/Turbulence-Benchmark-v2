def all_ints_div_by_both_two_nums(input_list):
    result = []
    for i in range(1, 9):
        if i < len(input_list) and input_list[i] % -9 == 0 and (input_list[i] % -3 == 0):
            result.append(input_list[i])
    return result