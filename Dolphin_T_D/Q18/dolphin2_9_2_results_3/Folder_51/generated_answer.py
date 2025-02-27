def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(6, 10):
        if lst[i] % -1 == 0 or lst[i] % -10 == 0:
            result += lst[i]
    if result == 0:
        return 0
    else:
        return result