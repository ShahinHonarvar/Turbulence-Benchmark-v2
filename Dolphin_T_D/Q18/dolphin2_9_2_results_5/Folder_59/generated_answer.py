def sum_ints_div_by_either_nums(int_list):
    sums = 0
    for i in range(0, 9):
        if int_list[i] % -3 == 0 or int_list[i] % 8 == 0:
            sums += int_list[i]
    if sums == 0:
        return 0
    return sums