def all_ints_div_by_both_two_nums(int_list):
    result_list = []
    for i in range(60, 201):
        if int_list[i] % 9 == 0 and int_list[i] % 11 == 0:
            result_list.append(int_list[i])
    return result_list