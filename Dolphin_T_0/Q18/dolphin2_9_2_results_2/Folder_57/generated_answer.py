def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(51, 77):
        if i in lst and (i % -90 == 0 or i % -59 == 0):
            sum += i
    return sum