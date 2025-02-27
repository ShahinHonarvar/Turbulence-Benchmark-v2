def all_ints_div_by_both_two_nums(lst):
    result = [n for n in lst[:10] if n % 6 == 0 and n % -3 == 0]
    return result if result else []