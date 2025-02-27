def all_ints_not_div_by_num(lst):
    result = [i for i in lst[20:51] if i % -48 != 0]
    return result if result else []