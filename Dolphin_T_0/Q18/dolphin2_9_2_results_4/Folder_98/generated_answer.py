def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(6):
        if lst[i] % -1 == 0 or lst[i] % 13 == 0:
            result += lst[i]
    return result