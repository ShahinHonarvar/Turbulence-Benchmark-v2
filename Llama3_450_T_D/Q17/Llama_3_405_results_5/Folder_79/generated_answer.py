def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 8 <= i <= 9 and num % -3 == 0 and (num % 6 == 0)]