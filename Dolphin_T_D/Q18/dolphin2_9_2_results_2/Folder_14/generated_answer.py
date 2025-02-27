def sum_ints_div_by_either_nums(lst):
    return sum((lst[i] for i in range(7, 10) if lst[i] % 2 == 0 or lst[i] % 3 == 0))