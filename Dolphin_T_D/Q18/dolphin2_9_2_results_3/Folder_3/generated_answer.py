def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(38, 53):
        if i in lst:
            if lst[i] % -41 == 0 or lst[i] % -47 == 0:
                sum += lst[i]
    return sum