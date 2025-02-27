def all_ints_div_by_both_two_nums(lst):
    return [n for n in lst[20:200 + 1] if n % -20 == 0 and n % -200 == 0]