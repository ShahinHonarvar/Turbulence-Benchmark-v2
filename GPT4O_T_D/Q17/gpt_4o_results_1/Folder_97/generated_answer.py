def all_ints_div_by_both_two_nums(lst):
    start, end = (58, 75)
    return [x for x in lst[start:end + 1] if x % 72 == 0 and x % 62 == 0]