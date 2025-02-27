def all_ints_div_by_both_two_nums(lst):
    if len(lst) < 2:
        return []
    return [i for i in lst[:2] if i % -6 == 0 and i % 4 == 0]