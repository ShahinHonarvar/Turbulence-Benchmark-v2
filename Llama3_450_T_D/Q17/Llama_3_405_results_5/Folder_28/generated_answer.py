def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 34 <= i <= 81 and num % 27 == 0 and (num % 57 == 0)]