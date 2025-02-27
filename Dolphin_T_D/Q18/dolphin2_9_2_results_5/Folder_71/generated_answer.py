def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(68, 100):
        if i in lst and (i % -37 == 0 or i % -26 == 0):
            total += i
    return total