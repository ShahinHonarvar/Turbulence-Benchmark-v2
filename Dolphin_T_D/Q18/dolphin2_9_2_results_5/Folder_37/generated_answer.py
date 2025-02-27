def sum_ints_div_by_either_nums(lst):
    return sum((lst[i] for i in range(2, 8) if lst[i] % -1 == 0 or lst[i] % -7 == 0))