def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(38, 53):
        if i < len(lst):
            if lst[i] % -41 == 0 or lst[i] % -47 == 0:
                total += lst[i]
    return total