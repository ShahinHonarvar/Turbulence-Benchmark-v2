def all_ints_div_by_num(lst):
    if len(lst) < 5:
        return []
    return [x for x in lst[4:5] if x % 3 == 0]