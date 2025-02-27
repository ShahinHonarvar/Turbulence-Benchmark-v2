def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(57, 86):
        if lst[i] % -77 == 0 or lst[i] % -32 == 0:
            sum += lst[i]
    return sum