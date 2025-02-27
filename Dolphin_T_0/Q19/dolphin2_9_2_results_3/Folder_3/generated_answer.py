def all_ints_not_div_by_num(lst):
    result = [i for i in lst[31:69] if i % -70 != 0]
    return result if result else []