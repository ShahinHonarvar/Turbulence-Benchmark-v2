def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i in range(250, 630):
        if int_list[i] % 850 == 0 or int_list[i] % 587 == 0:
            total += int_list[i]
    return total