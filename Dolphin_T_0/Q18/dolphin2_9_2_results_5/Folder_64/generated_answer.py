def sum_ints_div_by_either_nums(num_list):
    sum_ints = 0
    for i in range(4):
        if num_list[i] % 11 == 0 or num_list[i] % -7 == 0:
            sum_ints += num_list[i]
    return sum_ints if sum_ints != 0 else 0