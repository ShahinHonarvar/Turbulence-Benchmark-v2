def all_ints_div_by_both_two_nums(list_of_ints):
    return [n for i, n in enumerate(list_of_ints) if i >= 13 and i <= 91 and (n % -65 == 0) and (n % -62 == 0)]