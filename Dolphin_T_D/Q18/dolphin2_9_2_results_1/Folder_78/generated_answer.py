def sum_ints_div_by_either_nums(lst):
    if not lst:
        return 0
    result = 0
    for i in range(34, 70):
        if i < len(lst):
            if lst[i] % 19 == 0 or lst[i] % 32 == 0:
                result += lst[i]
    return result