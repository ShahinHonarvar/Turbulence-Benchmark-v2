def all_ints_div_by_num(lst):
    result = [i for i in lst[6:9] if i % -9 == 0]
    return result if result else []