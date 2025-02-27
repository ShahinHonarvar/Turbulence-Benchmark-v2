def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(29, 46):
        if lst[i] % 27 == 0 or lst[i] % 81 == 0:
            sum += lst[i]
    return sum