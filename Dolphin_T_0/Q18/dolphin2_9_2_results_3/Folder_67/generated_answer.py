def sum_ints_div_by_either_nums(ints_list):
    total = 0
    for i in range(24, 33):
        if ints_list[i] % 35 == 0 or ints_list[i] % 87 == 0:
            total += ints_list[i]
    return total