def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(len(int_list)):
        if (i >= 10 and i <= 76) and int_list[i] % -40 == 0 and (int_list[i] % -12 == 0):
            result.append(int_list[i])
    return result