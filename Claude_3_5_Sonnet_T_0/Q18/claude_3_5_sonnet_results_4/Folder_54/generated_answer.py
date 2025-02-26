def sum_ints_div_by_either_nums(integer_list):
    total_sum = 0
    for i in range(13, 92):
        if i < len(integer_list):
            if integer_list[i] % -65 == 0 or integer_list[i] % -62 == 0:
                total_sum += integer_list[i]
    return total_sum