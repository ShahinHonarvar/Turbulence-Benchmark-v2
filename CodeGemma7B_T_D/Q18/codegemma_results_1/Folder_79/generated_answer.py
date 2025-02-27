def sum_ints_div_by_either_nums(x):
    y = 0
    for i in range(8, 10):
        if i in x and (i % 3 == 0 or i % 6 == 0):
            y += i
    if y == 0:
        return 0
    else:
        return y