def sum_ints_div_by_either_nums(int_list):
    sum_div_num = 0
    for i in range(20, 201):
        if int_list[i] % -20 == 0 or int_list[i] % -200 == 0:
            sum_div_num += int_list[i]
    return sum_div_num