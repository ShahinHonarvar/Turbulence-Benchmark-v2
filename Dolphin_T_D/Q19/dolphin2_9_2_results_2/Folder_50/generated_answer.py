def all_ints_not_div_by_num(lst):
    result = [i for i in lst[13:76] if i % 44 != 0]
    return result if result else []