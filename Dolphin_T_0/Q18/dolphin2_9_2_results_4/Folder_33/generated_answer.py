def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(281, 695):
        if lst[i] % -722 == 0 or lst[i] % -731 == 0:
            total += lst[i]
    return total