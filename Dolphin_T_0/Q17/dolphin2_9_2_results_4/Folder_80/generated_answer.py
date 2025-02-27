def all_ints_div_by_both_two_nums(lst):
    result = [n for n in lst[14:94] if n % 71 == 0 and n % 81 == 0]
    return result if result else []