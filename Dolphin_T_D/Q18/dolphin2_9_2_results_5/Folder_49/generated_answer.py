def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(80, 201):
        if i % 10 == 0 or i % 1000 == 0:
            total += lst[i]
    return total