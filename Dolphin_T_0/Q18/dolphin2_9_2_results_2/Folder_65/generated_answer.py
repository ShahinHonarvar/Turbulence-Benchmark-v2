def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i in range(50, 93):
        if int_list[i] % -94 == 0 or int_list[i] % -95 == 0:
            total += int_list[i]
    return total if total != 0 else 0