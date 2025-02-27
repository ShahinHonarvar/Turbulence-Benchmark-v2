def all_ints_div_by_both_two_nums(lst):
    result = [n for n in lst[250:630] if n % 850 == 0 and n % 587 == 0]
    return result