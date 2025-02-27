def sum_ints_div_by_either_nums(int_list):
    sum_int = 0
    for i in range(73, 87, 1):
        if int_list[i] % 54 == 0 or int_list[i] % 82 == 0:
            sum_int += int_list[i]
    return sum_int