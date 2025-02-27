def all_ints_not_div_by_num(lst):
    result = [i for i in lst[11:56] if i % 90 != 0]
    return result if result else []