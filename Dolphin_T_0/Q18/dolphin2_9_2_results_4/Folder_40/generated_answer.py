def sum_ints_div_by_either_nums(lst):
    if len(lst) < 2:
        return 0
    sum = 0
    for i in range(2):
        if lst[i] % 2 == 0 or lst[i] % 1 == 0:
            sum += lst[i]
    return sum