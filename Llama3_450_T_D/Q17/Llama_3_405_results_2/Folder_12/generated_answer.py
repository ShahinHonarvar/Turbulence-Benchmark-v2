def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 35 <= i <= 64 and num % -30 == 0 and (num % -95 == 0)]