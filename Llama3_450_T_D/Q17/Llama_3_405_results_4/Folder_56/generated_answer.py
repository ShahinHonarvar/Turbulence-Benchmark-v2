def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 7 <= i <= 9 and num % -9 == 0 and (num % -7 == 0)]