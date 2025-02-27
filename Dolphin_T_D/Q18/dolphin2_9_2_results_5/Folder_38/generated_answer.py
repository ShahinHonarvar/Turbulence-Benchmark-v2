def sum_ints_div_by_either_nums(lst):
    if lst is None or len(lst) == 0 or len(lst) < 76:
        return 0
    result = 0
    for i in range(10, 77):
        if lst[i] % -40 == 0 or lst[i] % -12 == 0:
            result += lst[i]
    return result if result > 0 else 0