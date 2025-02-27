def all_ints_not_div_by_num(lst):
    result = [i for i in lst[32:70] if i % -70 != 0]
    return result