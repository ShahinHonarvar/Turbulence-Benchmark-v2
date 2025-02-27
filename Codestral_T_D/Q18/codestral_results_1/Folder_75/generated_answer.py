def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(20, 94):
        if lst[i] % -92 == 0 or lst[i] % -50 == 0:
            total += lst[i]
    return total