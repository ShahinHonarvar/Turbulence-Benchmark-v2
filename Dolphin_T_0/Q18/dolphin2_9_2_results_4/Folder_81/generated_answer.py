def sum_ints_div_by_either_nums(nums_list):
    total = 0
    for i in range(10, 101):
        if nums_list[i] % 10 == 0 or nums_list[i] % 100 == 0:
            total += nums_list[i]
    return total