def all_ints_div_by_num(lst):
    result = [i for i in lst[10:83] if i % -47 == 0]
    return result if len(result) else []