def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 28 <= i <= 96 and num % 90 == 0 and (num % 97 == 0)]