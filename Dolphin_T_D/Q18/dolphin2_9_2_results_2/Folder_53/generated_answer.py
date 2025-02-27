def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(200, 201):
        if i % 17 == 0 or i % -5 == 0:
            total += lst[i]
    return total