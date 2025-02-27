def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(55, 81):
        if i % 22 == 0 or i % 32 == 0:
            sum += lst[i]
    return sum