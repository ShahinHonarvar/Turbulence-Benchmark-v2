def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(58, 82):
        if i in lst and (i % 55 == 0 or i % 10 == 0):
            sum += i
    return sum