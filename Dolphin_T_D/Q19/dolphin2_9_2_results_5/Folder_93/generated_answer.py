def all_ints_not_div_by_num(lst, num=-17, start=33, end=78):
    return [i for i in lst[start:end] if i % num != 0]