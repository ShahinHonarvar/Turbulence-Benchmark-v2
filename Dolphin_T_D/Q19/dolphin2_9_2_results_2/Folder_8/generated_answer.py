def all_ints_not_div_by_num(lst, num=-75, start=17, end=88):
    return [i for i in lst[start:end] if i % num != 0]