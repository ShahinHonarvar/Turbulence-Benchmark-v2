def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(57, 86):
        if i < len(int_list):
            if int_list[i] % -77 == 0 and int_list[i] % -32 == 0:
                result.append(int_list[i])
    return result