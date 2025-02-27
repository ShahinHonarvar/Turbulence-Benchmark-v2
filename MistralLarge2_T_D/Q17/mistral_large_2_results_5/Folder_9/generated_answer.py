def all_ints_div_by_both_two_nums(lst):
    return [n for i, n in enumerate(lst) if 70 <= i <= 200 and n % 3 == 0 and (n % -300 == 0)]