def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(20, 36):
        if i != 23 and (lst[i] % -36 == 0 or lst[i] % -89 == 0):
            result += lst[i]
    return result