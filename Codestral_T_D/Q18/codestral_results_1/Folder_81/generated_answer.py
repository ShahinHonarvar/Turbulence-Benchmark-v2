def sum_ints_div_by_either_nums(lst):
    return sum((lst[i] for i in range(10, 101) if lst[i] % 10 == 0 or lst[i] % 100 == 0))