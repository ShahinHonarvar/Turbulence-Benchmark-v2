def all_ints_not_div_by_num(lst):
    result = [i for i in lst[15:57] if i % 86 != 0]
    return result if result else []