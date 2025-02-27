def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(86, 91):
        if lst[i] % -71 == 0 or lst[i] % -67 == 0:
            sum += lst[i]
    return sum