def all_ints_not_div_by_num(lst):
    return [i for idx, i in enumerate(lst) if 80 < idx < 200 and i % 1000 != 0]