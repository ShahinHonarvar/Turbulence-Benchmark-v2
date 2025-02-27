def sum_ints_div_by_either_nums(lst):
    return lst[0] if lst and (lst[0] % 1 == 0 or lst[0] % -1 == 0) else 0