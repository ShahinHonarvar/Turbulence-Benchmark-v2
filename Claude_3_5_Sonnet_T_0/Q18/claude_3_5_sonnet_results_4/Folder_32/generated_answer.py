def sum_ints_div_by_either_nums(integer_list):
    total_sum = 0
    for i in range(25, 96):
        if i < len(integer_list):
            if integer_list[i] % 51 == 0 or integer_list[i] % 77 == 0:
                total_sum += integer_list[i]
    return total_sum