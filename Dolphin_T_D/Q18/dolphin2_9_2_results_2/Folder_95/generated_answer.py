def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(57, 85):
        if lst[i] % -30 == 0 or lst[i] % -88 == 0:
            total += lst[i]
    return total if total != 0 else 0