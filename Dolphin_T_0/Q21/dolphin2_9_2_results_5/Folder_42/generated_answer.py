def all_ints_div_by_num(lst):
    result = [i for i in lst[31:93] if i % 20 == 0]
    return result if result else []