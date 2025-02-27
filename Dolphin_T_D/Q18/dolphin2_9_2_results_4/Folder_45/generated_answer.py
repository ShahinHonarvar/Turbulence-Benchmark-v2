def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(30, 201):
        if lst[i] % -115 == 0 or lst[i] % 115 == 0:
            sum += lst[i]
    return sum