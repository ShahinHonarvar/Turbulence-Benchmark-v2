def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(13, 77):
        if i in lst:
            if lst[i] % -66 == 0 or lst[i] % -32 == 0:
                total += lst[i]
    return total