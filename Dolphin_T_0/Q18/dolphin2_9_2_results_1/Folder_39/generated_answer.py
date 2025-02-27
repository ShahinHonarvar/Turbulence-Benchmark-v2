def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(13, 77):
        if lst[i] % -66 == 0 or lst[i] % -32 == 0:
            sum += lst[i]
    return sum