def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(42, 88):
        if lst[i] % -90 == 0 or lst[i] % -74 == 0:
            result += lst[i]
    return result