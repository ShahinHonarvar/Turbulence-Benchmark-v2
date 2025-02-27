def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(315, 935):
        if lst[i] % -897 == 0 or lst[i] % -556 == 0:
            result += lst[i]
    return result