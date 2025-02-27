def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(25, 81):
        if i % -20 == 0 or i % -26 == 0:
            result += lst[i]
    return result