def all_ints_not_div_by_num(l):
    return [j for i, j in enumerate(l) if 1 < i < 6 and j % 2 != 0]