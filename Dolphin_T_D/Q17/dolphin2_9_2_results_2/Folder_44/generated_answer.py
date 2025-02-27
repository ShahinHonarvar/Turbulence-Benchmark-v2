def all_ints_div_by_both_two_nums(input_list):
    result = []
    for i in range(25, 71):
        if input_list[i] % 74 == 0 and input_list[i] % 15 == 0:
            result.append(input_list[i])
    return result