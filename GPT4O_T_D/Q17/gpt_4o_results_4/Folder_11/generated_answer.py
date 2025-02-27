def all_ints_div_by_both_two_nums(lst):
    if len(lst) < 25:
        return []
    result = [x for x in lst[22:25] if x % -85 == 0 and x % -30 == 0]
    return result