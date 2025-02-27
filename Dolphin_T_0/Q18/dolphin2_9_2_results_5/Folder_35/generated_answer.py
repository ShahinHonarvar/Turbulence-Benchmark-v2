def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(77, 88):
        if i < len(lst):
            if lst[i] % 23 == 0 or lst[i] % 57 == 0:
                result += lst[i]
    return result