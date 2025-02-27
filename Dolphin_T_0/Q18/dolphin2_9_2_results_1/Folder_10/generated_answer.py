def sum_ints_div_by_either_nums(lst):
    if len(lst) < 99:
        return 0
    sum = 0
    for i in range(32, 100):
        if lst[i] % -11 == 0 or lst[i] % -15 == 0:
            sum += lst[i]
    return sum