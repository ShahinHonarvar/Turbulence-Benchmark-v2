def sum_ints_div_by_either_nums(num_list):
    sum = 0
    for i in range(6, 10):
        if num_list[i] % -1 == 0 or num_list[i] % -10 == 0:
            sum += num_list[i]
    if sum == 0:
        return 0
    else:
        return sum