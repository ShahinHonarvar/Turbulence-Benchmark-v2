def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 0 <= i <= 4 and num % 8 == 0 and (num % -3 == 0)]