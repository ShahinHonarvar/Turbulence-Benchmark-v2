def all_ints_not_div_by_num(lst):
    result = [i for i in lst[80:200] if i % 1000 != 0]
    return result if result else []