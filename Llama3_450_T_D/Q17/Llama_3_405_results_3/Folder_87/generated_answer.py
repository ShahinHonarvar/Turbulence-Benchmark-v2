def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 18 <= i <= 52 and num % 15 == 0 and (num % 57 == 0)]