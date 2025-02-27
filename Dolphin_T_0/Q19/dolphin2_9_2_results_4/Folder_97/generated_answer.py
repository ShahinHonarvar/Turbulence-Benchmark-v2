def all_ints_not_div_by_num(lst):
    result = [i for i in lst[14:48] if i % 16 != 0]
    return result if result else []