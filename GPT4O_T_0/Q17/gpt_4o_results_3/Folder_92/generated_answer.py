def all_ints_div_by_both_two_nums(lst):
    if not lst:
        return []
    return [x for x in lst[:1] if x % 1 == 0 and x % -1 == 0]