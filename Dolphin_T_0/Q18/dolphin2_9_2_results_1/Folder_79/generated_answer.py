def sum_ints_div_by_either_nums(lst):
    return sum((lst[i] for i in range(8, 10) if lst[i] % -3 == 0 or lst[i] % 6 == 0))