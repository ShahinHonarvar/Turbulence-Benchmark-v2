def sum_ints_div_by_either_nums(lst):
    total_sum = 0
    for i in range(543, 585):
        if lst[i] % -553 == 0 or lst[i] % -737 == 0:
            total_sum += lst[i]
    return total_sum