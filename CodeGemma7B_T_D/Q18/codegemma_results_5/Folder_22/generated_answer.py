def sum_ints_div_by_either_nums(int_list):
    sum = 0
    for i in range(40, 201):
        if int_list[i] % 21 == 0 or int_list[i] % 71 == 0:
            sum += int_list[i]
    return sum