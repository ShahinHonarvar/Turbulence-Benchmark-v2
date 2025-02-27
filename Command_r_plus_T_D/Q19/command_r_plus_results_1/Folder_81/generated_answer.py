def all_ints_not_div_by_num(lst):
    result = [i for i in lst[10:100] if i % 100 != 0]
    return result