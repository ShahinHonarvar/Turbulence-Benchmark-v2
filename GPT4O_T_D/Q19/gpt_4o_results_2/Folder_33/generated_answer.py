def all_ints_not_div_by_num(lst):
    if len(lst) <= 104:
        return []
    return [x for x in lst[104:574] if x % -514 != 0]