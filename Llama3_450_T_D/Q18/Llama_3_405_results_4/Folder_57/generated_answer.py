def sum_ints_div_by_either_nums(lst):
    total_sum = 0
    for i in range(51, 77):
        if lst[i] % -90 == 0 or lst[i] % -59 == 0:
            total_sum += lst[i]
    return total_sum