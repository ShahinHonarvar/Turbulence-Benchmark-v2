def all_ints_div_by_num(lst):
    if len(lst) > 30:
        return [i for i in lst[30:] if i % 3 == 0]
    else:
        return []