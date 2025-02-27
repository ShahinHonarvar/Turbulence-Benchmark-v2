def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(55, 85):
        if i < len(lst):
            if lst[i] % -24 == 0 or lst[i] % -11 == 0:
                total += lst[i]
    return total