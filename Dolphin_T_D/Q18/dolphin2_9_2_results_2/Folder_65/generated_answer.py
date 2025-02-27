def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(50, 93):
        if int_list[i] % -94 == 0 or int_list[i] % -95 == 0:
            sum += int_list[i]
    return sum