def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 10 <= i <= 76 and num % -40 == 0 and (num % -12 == 0)]