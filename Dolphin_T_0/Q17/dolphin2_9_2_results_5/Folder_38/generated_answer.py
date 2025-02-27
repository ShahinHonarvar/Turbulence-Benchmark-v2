def all_ints_div_by_both_two_nums(lst):
    result = [x for x in lst[10:77] if x % -40 == 0 and x % -12 == 0]
    if not result:
        return []
    return result