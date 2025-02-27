def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(1, 9):
        if lst[i] % -9 == 0 or lst[i] % -3 == 0:
            result += lst[i]
    return result