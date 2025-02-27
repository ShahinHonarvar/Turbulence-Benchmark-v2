def all_ints_div_by_both_two_nums(lst):
    result = [n for n in lst[:4] if n % 11 == 0 and n % -7 == 0]
    return result if result else []