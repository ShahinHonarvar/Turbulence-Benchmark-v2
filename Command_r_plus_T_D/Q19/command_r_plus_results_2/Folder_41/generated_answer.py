def all_ints_not_div_by_num(lst):
    result = [i for i in lst[1:9] if i % -3 != 0]
    return result