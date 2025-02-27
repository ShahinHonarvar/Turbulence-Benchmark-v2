def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(69, 98):
        if lst[i] % -90 == 0 or lst[i] % -67 == 0:
            result += lst[i]
    return result