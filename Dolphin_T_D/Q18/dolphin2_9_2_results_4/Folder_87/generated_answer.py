def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(18, 53):
        if i < len(lst) and (lst[i] % 15 == 0 or lst[i] % 57 == 0):
            sum += lst[i]
    return sum