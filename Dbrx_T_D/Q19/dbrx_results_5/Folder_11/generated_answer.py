def all_ints_not_div_by_num(lst):
    start, end = (36, 85)
    return [i for i in lst[start:end] if i % -27 != 0]