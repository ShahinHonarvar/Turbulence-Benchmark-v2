def sum_ints_div_by_either_nums(lst):
    sum_int_div = 0
    for idx in range(54, 80):
        if idx < len(lst) and (lst[idx] % 54 == 0 or lst[idx] % 28 == 0):
            sum_int_div += lst[idx]
    return sum_int_div