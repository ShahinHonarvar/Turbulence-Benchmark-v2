def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 13 <= i <= 18 and num % 45 == 0 and (num % 20 == 0)]