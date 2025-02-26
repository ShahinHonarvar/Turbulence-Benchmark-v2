def sum_ints_div_by_either_nums(int_list):
    result = 0
    for i in range(57, 86):
        if i < len(int_list):
            if int_list[i] % -77 == 0 or int_list[i] % -32 == 0:
                result += int_list[i]
    return result