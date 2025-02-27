def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 1 <= i <= 4 and num % 4 == 0 and (num % -6 == 0)]