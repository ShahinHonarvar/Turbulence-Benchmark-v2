def all_ints_not_div_by_num(lst):
    return [i for i in lst if i % 10 != 0 and 9 < lst.index(i) < len(lst) - 10]