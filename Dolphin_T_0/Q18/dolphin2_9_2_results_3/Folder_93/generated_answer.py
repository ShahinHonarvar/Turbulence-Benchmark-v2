def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(86, 90):
        if i in lst and (-61 in lst[i] or -79 in lst[i]):
            total += lst[i]
    return total or 0