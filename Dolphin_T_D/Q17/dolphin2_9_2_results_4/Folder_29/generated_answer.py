def all_ints_div_by_both_two_nums(lst):
    result = [n for n in lst[55:85] if n % -24 == 0 and n % -11 == 0]
    return result