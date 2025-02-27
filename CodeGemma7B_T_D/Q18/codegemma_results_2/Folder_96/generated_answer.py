def sum_ints_div_by_either_nums(num_list):
    total_sum = 0
    for i in range(50, 201):
        if num_list[i] % -34 == 0 or num_list[i] % 64 == 0:
            total_sum += num_list[i]
    return total_sum or 0