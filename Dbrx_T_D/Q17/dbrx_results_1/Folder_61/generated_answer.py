def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(min(6, len(int_list)) - 1):
        if int_list[i] % -5 == 0 and int_list[i] % -6 == 0:
            result.append(int_list[i])
    return result