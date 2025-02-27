def sum_ints_div_by_either_nums(num_list):
    sum = 0
    for i in range(0, 2):
        if num_list[i] % -6 == 0 or num_list[i] % 4 == 0:
            sum += num_list[i]
    return sum