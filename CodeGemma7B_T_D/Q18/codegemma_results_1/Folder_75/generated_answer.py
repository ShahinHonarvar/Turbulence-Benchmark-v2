def sum_ints_div_by_either_nums(num_list):
    total = 0
    for i in range(20, 94):
        if num_list[i] % 92 == 0 or num_list[i] % 50 == 0:
            total += num_list[i]
    if not total:
        return 0
    return total