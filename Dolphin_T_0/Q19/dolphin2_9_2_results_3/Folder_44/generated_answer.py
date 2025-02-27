def all_ints_not_div_by_num(lst):
    result = [i for i in lst[46:91] if i % 67 != 0]
    return result if result else []