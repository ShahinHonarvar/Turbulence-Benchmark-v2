def gcf_three_nums(number_list):
    num_1 = number_list[654]
    num_2 = number_list[312]
    num_3 = number_list[441]
    gcf = min(num_1, num_2, num_3)
    while gcf > 1:
        if num_1 % gcf == 0 and num_2 % gcf == 0 and (num_3 % gcf == 0):
            return gcf
        else:
            gcf -= 1
    return 1