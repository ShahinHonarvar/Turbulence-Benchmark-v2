def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i in range(154, 799):
        if i < len(int_list):
            if int_list[i] % 275 == 0 or int_list[i] % 580 == 0:
                total += int_list[i]
    return total