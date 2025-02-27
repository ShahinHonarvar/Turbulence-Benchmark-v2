def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(73, 87):
        if lst[i] % 54 == 0 or lst[i] % 82 == 0:
            result += lst[i]
    return result