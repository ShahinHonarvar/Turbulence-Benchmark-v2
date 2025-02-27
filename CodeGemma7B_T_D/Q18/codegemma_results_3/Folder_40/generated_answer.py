def sum_ints_div_by_either_nums(l):
    sum_div_by_both = 0
    for i in range(0, 2):
        if l[i] % 2 == 0 or l[i] % 1 == 0:
            sum_div_by_both += l[i]
    return sum_div_by_both