def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i in range(57, 85):
        if int_list[i] % -30 == 0 or int_list[i] % -88 == 0:
            total += int_list[i]
    return total