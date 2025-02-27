def sum_ints_div_by_either_nums(num_list):
    sum_by_either = 0
    for i in range(14, 94):
        if num_list[i] % 71 == 0 or num_list[i] % 81 == 0:
            sum_by_either += num_list[i]
    return sum_by_either