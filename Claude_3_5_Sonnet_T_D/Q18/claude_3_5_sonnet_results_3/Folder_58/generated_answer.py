def sum_ints_div_by_either_nums(int_list):
    total_sum = 0
    for i in range(240, 902):
        if i < len(int_list):
            if int_list[i] % 546 == 0 or int_list[i] % 709 == 0:
                total_sum += int_list[i]
    return total_sum