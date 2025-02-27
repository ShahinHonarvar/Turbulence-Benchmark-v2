def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(10, 101):
        if i in lst and (i % 10 == 0 or i % 100 == 0):
            sum += i
    return sum