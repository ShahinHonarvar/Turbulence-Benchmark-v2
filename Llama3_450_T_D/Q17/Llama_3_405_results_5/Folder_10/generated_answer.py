def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 32 <= i <= 99 and num % -11 == 0 and (num % -15 == 0)]