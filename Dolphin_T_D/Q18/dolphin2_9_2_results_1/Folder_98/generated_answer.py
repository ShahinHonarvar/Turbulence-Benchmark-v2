def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(0, 6):
        if i % -1 == 0 or i % 13 == 0:
            total += lst[i]
    return total