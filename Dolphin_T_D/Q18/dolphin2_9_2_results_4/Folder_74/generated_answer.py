def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i in range(90, 98):
        if i in int_list:
            if int_list[i] % 13 == 0 or int_list[i] % 35 == 0:
                total += int_list[i]
    return total