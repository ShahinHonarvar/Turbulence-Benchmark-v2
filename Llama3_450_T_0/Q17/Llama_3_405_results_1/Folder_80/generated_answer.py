def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 14 <= i <= 93 and num % 71 == 0 and (num % 81 == 0)]