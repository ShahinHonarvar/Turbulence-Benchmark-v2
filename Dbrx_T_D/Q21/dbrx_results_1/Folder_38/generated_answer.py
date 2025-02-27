def all_ints_div_by_num(lst):
    if len(lst) < 15:
        return []
    return [i for i in lst[12:16] if i % -80 == 0]