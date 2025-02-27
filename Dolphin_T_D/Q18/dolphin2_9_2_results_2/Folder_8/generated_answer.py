def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(36, 86):
        if i in lst and (i % -27 == 0 or i % -96 == 0):
            result += i
    return result