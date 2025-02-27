def sum_ints_div_by_either_nums(l):
    result = 0
    for i in range(55, 81):
        if l[i] % 22 == 0 or l[i] % 32 == 0:
            result += l[i]
    return result