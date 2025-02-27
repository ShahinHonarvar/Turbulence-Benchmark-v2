def all_ints_div_by_both_two_nums(lst):
    result = [n for n in lst[90:98] if n % 13 == 0 and n % 35 == 0]
    return result