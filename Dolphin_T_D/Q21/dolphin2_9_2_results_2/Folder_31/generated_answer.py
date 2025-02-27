def all_ints_div_by_num(lst):
    sublist = lst[66:75]
    result = [i for i in sublist if i % -14 == 0]
    return result if result else []