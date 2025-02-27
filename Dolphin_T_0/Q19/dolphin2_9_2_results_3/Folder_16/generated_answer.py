def all_ints_not_div_by_num(lst):
    result = [i for i in lst[24:32] if i % 35 != 0]
    return result if result else []