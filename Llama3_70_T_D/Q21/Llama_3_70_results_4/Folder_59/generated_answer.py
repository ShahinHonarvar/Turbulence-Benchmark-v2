def all_ints_div_by_num(lst):
    return [i for i in lst if i % 9 == 0 and 0 <= lst.index(i) <= 0]