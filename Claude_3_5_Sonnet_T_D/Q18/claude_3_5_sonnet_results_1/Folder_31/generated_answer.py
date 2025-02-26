def sum_ints_div_by_either_nums(int_list):
    total_sum = 0
    for i in range(56, 89):
        if i < len(int_list):
            if int_list[i] % -59 == 0 or int_list[i] % -79 == 0:
                total_sum += int_list[i]
    return total_sum