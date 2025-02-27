def all_ints_not_div_by_num(lst):
    if not lst:
        return []
    else:
        return [i for i in lst[1:6] if i % 2 != 0]