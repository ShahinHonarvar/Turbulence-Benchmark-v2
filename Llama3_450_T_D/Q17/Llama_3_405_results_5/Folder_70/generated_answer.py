def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 42 <= i <= 43 and num % 15 == 0 and (num % 87 == 0)]