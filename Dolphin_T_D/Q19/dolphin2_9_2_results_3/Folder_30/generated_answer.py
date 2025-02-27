def all_ints_not_div_by_num(lst):
    result = [i for i in lst[20:35] if i % 36 != 0 and i % -36 != 0]
    return result if result else []