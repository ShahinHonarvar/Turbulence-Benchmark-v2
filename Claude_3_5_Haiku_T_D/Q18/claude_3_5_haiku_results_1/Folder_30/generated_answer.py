def sum_ints_div_by_either_nums(num_list):
    total = 0
    for i in range(11, 77):
        if i < len(num_list) and (num_list[i] % -81 == 0 or num_list[i] % -94 == 0):
            total += num_list[i]
    return total