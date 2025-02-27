def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(38, 82):
        if lst[i] % -61 == 0 or lst[i] % -71 == 0:
            total += lst[i]
    return total if total != 0 else 0