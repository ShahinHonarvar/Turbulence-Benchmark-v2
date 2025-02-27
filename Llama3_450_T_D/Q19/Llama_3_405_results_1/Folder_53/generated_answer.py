def all_ints_not_div_by_num(lst):
    result = [i for i in lst[199:201] if i % -200 != 0]
    return [i for i in result if isinstance(i, int)]