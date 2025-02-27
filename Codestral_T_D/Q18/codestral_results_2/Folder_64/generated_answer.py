def sum_ints_div_by_either_nums(num_list):
    sum = 0
    for i in range(4):
        if num_list[i] % 11 == 0 or num_list[i] % -7 == 0:
            sum += num_list[i]
    return sum