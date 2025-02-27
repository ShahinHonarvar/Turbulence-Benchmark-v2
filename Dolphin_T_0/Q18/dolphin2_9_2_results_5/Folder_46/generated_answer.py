def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(11, 47):
        if lst[i] % 36 == 0 or lst[i] % 55 == 0:
            result += lst[i]
    return result if result != 0 else 0