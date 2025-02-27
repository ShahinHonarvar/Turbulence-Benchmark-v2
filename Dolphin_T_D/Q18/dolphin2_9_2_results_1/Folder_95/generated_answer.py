def sum_ints_div_by_either_nums(ints_list):
    ints_sum = 0
    for i in range(57, 85):
        if ints_list[i] % -30 == 0 or ints_list[i] % -88 == 0:
            ints_sum += ints_list[i]
    return ints_sum