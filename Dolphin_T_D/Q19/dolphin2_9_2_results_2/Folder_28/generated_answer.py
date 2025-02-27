def all_ints_not_div_by_num(lst):
    result = [i for i in lst[81:86] if i % 77 != 0]
    return result if result else []