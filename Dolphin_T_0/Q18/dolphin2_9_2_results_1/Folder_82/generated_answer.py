def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(20, 201):
        if i % -20 == 0 or i % -200 == 0:
            total += lst[i]
    return total if total != 0 else 0