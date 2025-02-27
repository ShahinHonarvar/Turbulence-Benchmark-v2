def all_ints_not_div_by_num(lst):
    result = [x for x in lst[31:69] if x % -70 != 0]
    return result if len(result) > 0 else []