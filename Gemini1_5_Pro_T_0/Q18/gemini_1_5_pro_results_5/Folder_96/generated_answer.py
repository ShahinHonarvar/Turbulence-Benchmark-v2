def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(50, 201):
        if i < len(lst) and (lst[i] % -34 == 0 or lst[i] % 64 == 0):
            sum += lst[i]
    return sum