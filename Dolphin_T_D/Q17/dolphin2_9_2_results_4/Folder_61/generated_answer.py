def all_ints_div_by_both_two_nums(l):
    result = [n for n in l[:7] if n % -5 == 0 and n % -6 == 0]
    return result if result else []