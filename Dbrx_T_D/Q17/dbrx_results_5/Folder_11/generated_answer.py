def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(len(int_list)):
        if i >= 22 and i <= 24 and (int_list[i] % -85 == 0) and (int_list[i] % -30 == 0):
            result.append(int_list[i])
    return result