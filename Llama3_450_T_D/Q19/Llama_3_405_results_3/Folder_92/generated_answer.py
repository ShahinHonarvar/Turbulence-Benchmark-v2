def all_ints_not_div_by_num(lst):
    return [i for i in range(1, lst[1]) if i not in [j for j in range(lst[0] + 1, lst[1]) if j % -1 == 0]]