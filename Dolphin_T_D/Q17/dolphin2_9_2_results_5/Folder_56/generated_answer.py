def all_ints_div_by_both_two_nums(l):
    result = []
    for i in range(7, 10):
        if l[i] % -9 == 0 and l[i] % -7 == 0:
            result.append(l[i])
    return result