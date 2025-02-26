def sum_ints_div_by_either_nums(integer_list):
    if len(integer_list) < 80:
        return 0
    total_sum = 0
    for i in range(54, 80):
        if integer_list[i] % 54 == 0 or integer_list[i] % 28 == 0:
            total_sum += integer_list[i]
    return total_sum