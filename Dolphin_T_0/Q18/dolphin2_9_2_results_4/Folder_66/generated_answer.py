def sum_ints_div_by_either_nums(lst):
    return sum((lst[i] for i in range(58, 82) if lst[i] % 55 == 0 or lst[i] % 10 == 0))