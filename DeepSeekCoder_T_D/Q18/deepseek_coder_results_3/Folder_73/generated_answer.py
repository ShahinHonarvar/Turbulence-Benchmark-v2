def sum_ints_div_by_either_nums(int_list):
    if 81 <= len(int_list) - 1 < 86:
        return 0
    sum_divisible = 0
    for i in range(81, min(87, len(int_list))):
        if int_list[i] % -33 == 0 or int_list[i] % -62 == 0:
            sum_divisible += int_list[i]
    return sum_divisible