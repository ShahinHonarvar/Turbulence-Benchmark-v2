def all_ints_not_div_by_num(lst, start=11, end=56):
    return [i for i in lst[start:end] if i % 90 != 0]