def all_ints_not_div_by_num(lst):
    sublist = lst[200:202]
    result = [i for i in sublist if i % -200 != 0]
    return result if result else []