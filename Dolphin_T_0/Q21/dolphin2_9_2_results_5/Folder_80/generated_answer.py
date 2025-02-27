def all_ints_div_by_num(lst):
    result = [i for i in lst[27:87] if i % 29 == 0]
    return result if result else []