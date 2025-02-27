def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(5):
        if i % 8 == 0 or i % -3 == 0:
            result += lst[i]
    return result