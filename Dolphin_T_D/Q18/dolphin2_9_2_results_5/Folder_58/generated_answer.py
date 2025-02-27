def sum_ints_div_by_either_nums(ints_list):
    total = 0
    for i in range(240, 902):
        if ints_list[i] % 546 == 0 or ints_list[i] % 709 == 0:
            total += ints_list[i]
    return total