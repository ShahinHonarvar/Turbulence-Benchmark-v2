def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(81, 87):
        if i < len(lst):
            if lst[i] % -33 == 0 or lst[i] % -62 == 0:
                result += lst[i]
    return result