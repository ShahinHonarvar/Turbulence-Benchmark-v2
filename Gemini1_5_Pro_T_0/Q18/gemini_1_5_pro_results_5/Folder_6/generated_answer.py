def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(41, 57):
        if i < len(lst) and (lst[i] % 82 == 0 or lst[i] % 90 == 0):
            sum += lst[i]
    return sum