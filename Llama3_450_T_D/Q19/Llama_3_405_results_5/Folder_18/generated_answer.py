def all_ints_not_div_by_num(lst):
    return [i for i in range(35, 98) if i not in [j for j in lst if j % 41 == 0]]