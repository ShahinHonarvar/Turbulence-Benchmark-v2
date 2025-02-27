def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(57, 85):
        if i < len(lst) and (lst[i] % -30 == 0 or lst[i] % -88 == 0):
            sum += lst[i]
    return sum