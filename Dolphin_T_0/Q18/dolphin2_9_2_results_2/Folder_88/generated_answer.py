def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(3, 10):
        if i < len(lst) and (lst[i] % 6 == 0 or lst[i] % 1 == 0):
            sum += lst[i]
    return sum