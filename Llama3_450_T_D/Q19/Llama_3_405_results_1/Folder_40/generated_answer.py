def all_ints_not_div_by_num(lst):
    return [i for i in range(1, lst[0]) if all((i % j != 0 for j in lst[1:]))]