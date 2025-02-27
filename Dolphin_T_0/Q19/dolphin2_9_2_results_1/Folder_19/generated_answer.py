def all_ints_not_div_by_num(lst):
    if 4 >= len(lst) or 5 >= len(lst):
        return []
    result = [x for x in lst[4:5] if x % -7 != 0]
    return result