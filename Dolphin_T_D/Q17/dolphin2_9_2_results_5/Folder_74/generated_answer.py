def all_ints_div_by_both_two_nums(lst):
    vals = lst[90:98]
    result = [x for x in vals if x % 13 == 0 and x % 35 == 0]
    if len(result) == 0:
        return []
    else:
        return result