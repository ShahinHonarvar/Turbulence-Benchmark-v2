def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(58, 76):
        if i in lst and (i % 72 == 0 or i % 62 == 0):
            sum += i
    return sum