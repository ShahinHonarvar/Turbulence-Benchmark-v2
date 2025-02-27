def sum_ints_div_by_either_nums(lst):
    if 200 >= len(lst):
        return 0
    if lst[200] % 17 == 0 or lst[200] % -5 == 0:
        return lst[200]
    return 0