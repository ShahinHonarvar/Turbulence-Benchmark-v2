def sum_ints_div_by_either_nums(l):
    result = 0
    for i in range(20, 36):
        if l[i] % -36 == 0 or l[i] % -89 == 0:
            result += l[i]
    return result