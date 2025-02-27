def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(57, 86):
        if i in lst and (i % -77 == 0 or i % -32 == 0):
            total += i
    return total