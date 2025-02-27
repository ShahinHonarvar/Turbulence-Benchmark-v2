def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 40 <= i <= 200 and num % 21 == 0 and (num % 71 == 0)]