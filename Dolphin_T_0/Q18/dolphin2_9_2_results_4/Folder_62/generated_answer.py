def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(44, 60):
        if i < len(lst) and (lst[i] % 39 == 0 or lst[i] % 15 == 0):
            result += lst[i]
    return result