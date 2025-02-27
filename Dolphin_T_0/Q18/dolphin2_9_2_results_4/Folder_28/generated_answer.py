def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(34, 82):
        if i in lst:
            if i % 27 == 0 or i % 57 == 0:
                sum += i
    return sum