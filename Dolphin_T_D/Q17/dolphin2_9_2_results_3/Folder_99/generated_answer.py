def all_ints_div_by_both_two_nums(lst):
    result = [n for n in lst[154:799] if n % 275 == 0 and n % 580 == 0]
    return result