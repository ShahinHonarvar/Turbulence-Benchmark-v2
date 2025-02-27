def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(42, 88):
        if i in lst and (i % -90 == 0 or i % -74 == 0):
            sum += i
    return sum