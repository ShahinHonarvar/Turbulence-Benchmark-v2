def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(70, 201):
        if i in lst and (i % 3 == 0 or i % -300 == 0):
            sum += i
    return sum