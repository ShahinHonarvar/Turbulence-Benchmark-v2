def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(154, 799):
        if i % 275 == 0 or i % 580 == 0:
            total += lst[i]
    return total