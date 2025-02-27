def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(36, 86):
        if i in lst and (i % -27 == 0 or i % -96 == 0):
            total += i
    return total