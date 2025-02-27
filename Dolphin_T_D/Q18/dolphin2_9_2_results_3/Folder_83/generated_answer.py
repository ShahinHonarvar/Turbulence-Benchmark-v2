def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(90, 201):
        if lst[i] % -31 == 0 or lst[i] % 13 == 0:
            result += lst[i]
    return result if result != 0 else None