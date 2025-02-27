def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(48, 60):
        if i in lst and (i % 88 == 0 or i % 58 == 0):
            sum += i
    return sum