def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(len(lst)):
        if i <= 8 and (lst[i] % -3 == 0 or lst[i] % 8 == 0):
            result += lst[i]
    return result