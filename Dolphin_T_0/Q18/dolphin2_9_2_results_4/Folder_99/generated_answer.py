def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(154, 799):
        if i in lst and (i % 275 == 0 or i % 580 == 0):
            result += i
    return result