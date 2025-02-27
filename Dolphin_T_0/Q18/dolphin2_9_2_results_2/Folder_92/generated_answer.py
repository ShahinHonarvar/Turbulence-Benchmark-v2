def sum_ints_div_by_either_nums(lst):
    return sum((lst[i] for i in range(len(lst)) if lst[i] % 1 == 0 or lst[i] % -1 == 0))