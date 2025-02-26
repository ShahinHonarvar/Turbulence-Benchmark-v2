def sum_ints_div_by_either_nums(integer_list):
    total_sum = 0
    for i in range(51, 77):
        if i < len(integer_list):
            if integer_list[i] % -90 == 0 or integer_list[i] % -59 == 0:
                total_sum += integer_list[i]
    return total_sum