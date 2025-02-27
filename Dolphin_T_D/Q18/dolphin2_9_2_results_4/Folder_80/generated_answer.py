def sum_ints_div_by_either_nums(l):
    total = 0
    for i in range(14, 94):
        if l[i] % 71 == 0 or l[i] % 81 == 0:
            total += l[i]
    return total