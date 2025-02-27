def all_ints_div_by_num(lst):
    result = [i for i in lst[11:83] if i % -47 == 0]
    return result if result else []