def all_ints_not_div_by_num(lst):
    result = [i for i in lst[19:94] if i % -32 != 0]
    return result if result else []